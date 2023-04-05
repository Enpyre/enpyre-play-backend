from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    SerializerMethodField,
    ValidationError,
)

from enpyre_play.users.serializers import UserSerializer

from .models import Quizz, QuizzAnswer, QuizzQuestion, QuizzUserAnswer


class QuizzAnswerSerializer(ModelSerializer):
    question_id = PrimaryKeyRelatedField(
        source='question', queryset=QuizzQuestion.objects.all(), required=False
    )
    quizz_id = PrimaryKeyRelatedField(
        source='question.quizz', queryset=Quizz.objects.all(), required=False
    )

    class Meta:
        model = QuizzAnswer
        fields = (
            'id',
            'title',
            'content',
            'is_correct',
            'score_amount',
            'position',
            'question_id',
            'quizz_id',
        )
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if request and instance.question.quizz.owner_id != request.user.id:
            raise ValidationError('You are not the owner of this quizz')
        return super().update(instance, validated_data)


class QuizzQuestionSerializer(ModelSerializer):
    quizz_id = PrimaryKeyRelatedField(source='quizz', queryset=Quizz.objects.all(), required=False)
    answers = QuizzAnswerSerializer(many=True, required=False)
    user_answers = SerializerMethodField()

    class Meta:
        model = QuizzQuestion
        fields = ('id', 'title', 'content', 'position', 'quizz_id', 'answers', 'user_answers')
        read_only_fields = ('id', 'user_answers')

    def get_user_answers(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return []
        return (
            QuizzUserAnswer.objects.filter(answer__question=obj, user=request.user)
            .order_by('answer_id')
            .distinct('answer_id')
            .values_list('answer_id', flat=True)
        )

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if request and instance.quizz.owner_id != request.user.id:
            raise ValidationError('You are not the owner of this quizz')
        return super().update(instance, validated_data)


class QuizzSerializer(ModelSerializer):
    owner = UserSerializer(read_only=True, exclude_fields=('email',))
    questions = QuizzQuestionSerializer(many=True, required=False)

    class Meta:
        model = Quizz
        fields = ('id', 'title', 'description', 'quizz_type', 'owner', 'questions')
        read_only_fields = ('id', 'owner')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('questions', None)
        return data

    def update(self, instance, validated_data):
        if instance.owner_id != validated_data['owner']:
            raise ValidationError('You are not the owner of this quizz')
        return super().update(instance, validated_data)

    def create(self, validated_data):
        questions = validated_data.pop('questions', [])
        quizz = Quizz.objects.create(**validated_data)
        for question in questions:
            answers = question.pop('answers', [])
            question.pop('quizz_id', None)
            question = QuizzQuestion.objects.create(**question, quizz=quizz)
            for answer in answers:
                answer.pop('question_id', None)
                answer.pop('quizz_id', None)
                QuizzAnswer.objects.create(**answer, question=question)
        return quizz


class QuizzUserAnswerSerializer(ModelSerializer):
    quizz_id = PrimaryKeyRelatedField(source='answer.question.quizz', read_only=True)
    question_id = PrimaryKeyRelatedField(source='answer.question', read_only=True)
    answer_id = PrimaryKeyRelatedField(source='answer', queryset=QuizzAnswer.objects.all())
    user_id = PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model = QuizzUserAnswer
        fields = ('id', 'answer_id', 'user_id', 'quizz_id', 'question_id')
        read_only_fields = ('id', 'user_id', 'quizz_id', 'question_id')

    # def create(self, validated_data):
    #     return super().create(validated_data)
