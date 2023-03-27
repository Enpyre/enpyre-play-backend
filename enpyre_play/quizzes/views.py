from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Quizz, QuizzAnswer, QuizzQuestion, QuizzUserAnswer
from .serializers import (
    QuizzAnswerSerializer,
    QuizzQuestionSerializer,
    QuizzSerializer,
    QuizzUserAnswerSerializer,
)


class QuizzViewSet(ModelViewSet):
    queryset = Quizz.objects.all()
    serializer_class = QuizzSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'description')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class QuizzQuestionViewSet(ModelViewSet):
    serializer_class = QuizzQuestionSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'content')

    def get_queryset(self):
        return QuizzQuestion.objects.filter(
            quizz__id=self.kwargs['quizz_pk'],
        )

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            data = request.data.copy()
            for item in data:
                item['quizz_id'] = kwargs['quizz_pk']
                serializer = self.get_serializer(data=item)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
            return self.list(request, *args, **kwargs)
        return super().create(request, *args, **kwargs)


class QuizzAnswerViewSet(ModelViewSet):
    serializer_class = QuizzAnswerSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'content')

    def get_queryset(self):
        return QuizzAnswer.objects.filter(
            question__id=self.kwargs['question_pk'],
            question__quizz__id=self.kwargs['quizz_pk'],
        )

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            data = request.data.copy()
            for item in data:
                item['question_id'] = kwargs['question_pk']
                serializer = self.get_serializer(data=item)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
            return self.list(request, *args, **kwargs)
        return super().create(request, *args, **kwargs)


class QuizzUserAnswerViewSet(ModelViewSet):
    serializer_class = QuizzUserAnswerSerializer
    permission_classes = (IsAuthenticated,)
    # filter_backends = (SearchFilter,)
    # search_fields = ('answer__title', 'answer__content')

    def get_queryset(self):
        return QuizzUserAnswer.objects.filter(
            user=self.request.user,
        )

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            data = request.data.copy()
            for item in data:
                serializer = self.get_serializer(data=item)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
            return self.list(request, *args, **kwargs)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
