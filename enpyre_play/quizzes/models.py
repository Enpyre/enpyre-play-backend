from django.db import models

from enpyre_play.models import BaseModel
from enpyre_play.users.models import User
from enpyre_play.users.utils import get_sentinel_user


class Quizz(BaseModel):
    title = models.CharField(max_length=100, help_text='Title of the quizz')
    description = models.TextField(null=True, blank=True, help_text='Description of the quizz')
    quizz_type = models.CharField(max_length=100, help_text='Type of the quizz')

    owner = models.ForeignKey(
        User,
        on_delete=models.SET(get_sentinel_user),
        related_name='quizzes',
    )


class QuizzQuestion(BaseModel):
    title = models.CharField(max_length=100, help_text='Title of the question')
    content = models.TextField(null=True, blank=True, help_text='Content of the question')
    position = models.IntegerField(default=0, help_text='Position of the question')

    quizz = models.ForeignKey(
        Quizz,
        on_delete=models.CASCADE,
        related_name='questions',
    )


class QuizzAnswer(BaseModel):
    title = models.CharField(max_length=100, help_text='Title of the answer')
    content = models.TextField(null=True, blank=True, help_text='Content of the answer')
    is_correct = models.BooleanField(default=False, help_text='Is the answer correct')
    score_amount = models.IntegerField(default=0, help_text='Score amount of the answer')
    position = models.IntegerField(default=0, help_text='Position of the answer')

    question = models.ForeignKey(
        QuizzQuestion,
        on_delete=models.CASCADE,
        related_name='answers',
    )


class QuizzUserAnswer(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='quizz_answers',
    )
    answer = models.ForeignKey(
        QuizzAnswer,
        on_delete=models.CASCADE,
        related_name='user_answers',
    )
