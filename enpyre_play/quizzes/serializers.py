from django.db import transaction
from rest_framework.serializers import (
    IntegerField,
    ListSerializer,
    ModelSerializer,
    ValidationError,
)

from enpyre_play.users.serializers import UserSerializer

from .models import Quizz, QuizzAnswer, QuizzQuestion


class QuizzAnswerListSerializer(ListSerializer):
    @transaction.atomic
    def create(self, validated_data):
        answers = [QuizzAnswer(**item) for item in validated_data]
        return QuizzAnswer.objects.bulk_create(answers)

    @transaction.atomic
    def update(self, instance, validated_data):
        answer_mapping = {answer.id: answer for answer in instance}
        data_mapping = {item.get('id'): item for item in validated_data}
        print('QuizzAnswerListSerializer update', validated_data)

        ret = []
        for answer_id, data in data_mapping.items():
            answer = answer_mapping.get(answer_id, None)
            if answer is None:
                raise ValidationError(f'Answer with id {answer_id} does not exist')
            for attr, value in data.items():
                setattr(answer, attr, value)
            answer.save()
            ret.append(answer)

        for answer in instance:
            if answer.id not in data_mapping:
                answer.delete()

        return ret


class QuizzAnswerSerializer(ModelSerializer):
    id = IntegerField(required=False, allow_null=True)

    class Meta:
        model = QuizzAnswer
        fields = ('id', 'title', 'content', 'is_correct', 'score_amount', 'position')
        list_serializer_class = QuizzAnswerListSerializer
        read_only_fields = ('id',)


class QuizzQuestionListSerializer(ListSerializer):
    def create(self, validated_data):
        questions = [QuizzQuestion(**item) for item in validated_data]
        return QuizzQuestion.objects.bulk_create(questions)

    @transaction.atomic
    def update(self, instance, validated_data):
        question_mapping = {question.id: question for question in instance}
        data_mapping = {item.get('id'): item for item in validated_data}
        print('QuizzQuestionListSerializer update', validated_data)

        ret = []
        for question_id, data in data_mapping.items():
            question = question_mapping.get(question_id, None)
            if question is None:
                raise ValidationError(f'Question with id {question_id} does not exist')
            for attr, value in data.items():
                setattr(question, attr, value)
            question.save()
            ret.append(question)

        for question in instance:
            if question.id not in data_mapping:
                question.delete()

        return ret


class QuizzQuestionSerializer(ModelSerializer):
    id = IntegerField(required=False, allow_null=True)
    answers = QuizzAnswerSerializer(many=True)

    class Meta:
        model = QuizzQuestion
        fields = ('id', 'title', 'content', 'position', 'answers')
        list_serializer_class = QuizzQuestionListSerializer
        read_only_fields = ('id',)


class QuizzSerializer(ModelSerializer):
    id = IntegerField(required=False, allow_null=True)
    questions = QuizzQuestionSerializer(many=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Quizz
        fields = ('id', 'title', 'description', 'quizz_type', 'owner', 'questions')

    @transaction.atomic
    def create(self, validated_data):
        questions_data = validated_data.pop('questions')

        quizz = Quizz.objects.create(**validated_data)

        for question_data in questions_data:
            answers_data = question_data.pop('answers')
            question = QuizzQuestion.objects.create(quizz=quizz, **question_data)
            for answer_data in answers_data:
                QuizzAnswer.objects.create(question=question, **answer_data)

        return quizz

    @transaction.atomic
    def update(self, instance, validated_data):
        request = self.context.get('request')
        if instance.owner_id != request.user.id:
            raise ValidationError('You are not the owner of this quizz')

        try:
            questions_data = validated_data.pop('questions')
        except KeyError:
            questions_data = []

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.quizz_type = validated_data.get('quizz_type', instance.quizz_type)
        instance.save()

        updated_questions = []
        for question_data in questions_data:
            try:
                answers_data = question_data.pop('answers')
            except KeyError:
                answers_data = []
            if 'id' in question_data:
                question = QuizzQuestion.objects.get(id=question_data['id'])
                question.title = question_data.get('title', question.title)
                question.content = question_data.get('content', question.content)
                question.position = question_data.get('position', question.position)
                question.save()
            else:
                question = QuizzQuestion.objects.create(quizz=instance, **question_data)

            updated_questions.append(question.id)

            for answer_data in answers_data:
                if 'id' in answer_data:
                    answer = QuizzAnswer.objects.get(id=answer_data['id'])
                    answer.title = answer_data.get('title', answer.title)
                    answer.content = answer_data.get('content', answer.content)
                    answer.is_correct = answer_data.get('is_correct', answer.is_correct)
                    answer.score_amount = answer_data.get('score_amount', answer.score_amount)
                    answer.position = answer_data.get('position', answer.position)
                    answer.save()
                else:
                    QuizzAnswer.objects.create(question=question, **answer_data)

        if not self.partial:
            for question in instance.questions.all():
                if question.id not in updated_questions:
                    question.delete()

        return instance
