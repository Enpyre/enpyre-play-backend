from celery import group, shared_task
from enpyre_play.tasks import BaseTaskWithRetry

from .enums import ScoreTypeSet
from .models import Score, UserScore


@shared_task(bind=True, ignore_results=True, base=BaseTaskWithRetry)
def compute_weekly_score(self, user_id: int, score_amount: int):
    score = Score.build(ScoreTypeSet.WEEKLY)
    user_score = UserScore.build(user_id, score)
    user_score.compute(score_amount)


@shared_task(bind=True, ignore_results=True, base=BaseTaskWithRetry)
def compute_monthly_score(self, user_id: int, score_amount: int):
    score = Score.build(ScoreTypeSet.MONTHLY)
    user_score = UserScore.build(user_id, score)
    user_score.compute(score_amount)


@shared_task(bind=True, ignore_results=True, base=BaseTaskWithRetry)
def compute_yearly_score(self, user_id: int, score_amount: int):
    score = Score.build(ScoreTypeSet.YEARLY)
    user_score = UserScore.build(user_id, score)
    user_score.compute(score_amount)


@shared_task(bind=True, ignore_results=True, base=BaseTaskWithRetry)
def compute_global_score(self, user_id: int, score_amount: int):
    score = Score.build(ScoreTypeSet.GLOBAL)
    user_score = UserScore.build(user_id, score)
    user_score.compute(score_amount)


@shared_task(ignore_results=True)
def compute_score(user_id: int, score_amount: int):
    compute_tasks = group(
        compute_weekly_score.s(user_id, score_amount),
        compute_monthly_score.s(user_id, score_amount),
        compute_yearly_score.s(user_id, score_amount),
        compute_global_score.s(user_id, score_amount),
    )
    compute_tasks.apply_async()
