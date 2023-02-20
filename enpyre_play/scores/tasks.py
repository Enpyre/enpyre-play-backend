from django.db import transaction

from celery import group, shared_task

from .enums import ScoreTypeSet
from .models import Score, UserScore


@shared_task
def compute_weekly_score(user_id: int, score_amount: int):
    with transaction.atomic(durable=True):
        score = Score.build(ScoreTypeSet.WEEKLY)
        user_score = UserScore.build(user_id, score)
        user_score.compute(score_amount)


@shared_task
def compute_monthly_score(user_id: int, score_amount: int):
    with transaction.atomic(durable=True):
        score = Score.build(ScoreTypeSet.MONTHLY)
        user_score = UserScore.build(user_id, score)
        user_score.compute(score_amount)


@shared_task
def compute_yearly_score(user_id: int, score_amount: int):
    with transaction.atomic(durable=True):
        score = Score.build(ScoreTypeSet.YEARLY)
        user_score = UserScore.build(user_id, score)
        user_score.compute(score_amount)


@shared_task
def compute_global_score(user_id: int, score_amount: int):
    with transaction.atomic(durable=True):
        score = Score.build(ScoreTypeSet.GLOBAL)
        user_score = UserScore.build(user_id, score)
        user_score.compute(score_amount)


@shared_task
def compute_score(user_id: int, score_amount: int):
    compute_tasks = group(
        compute_weekly_score.s(user_id, score_amount),
        compute_monthly_score.s(user_id, score_amount),
        compute_yearly_score.s(user_id, score_amount),
        compute_global_score.s(user_id, score_amount),
    )
    compute_tasks.apply_async()
