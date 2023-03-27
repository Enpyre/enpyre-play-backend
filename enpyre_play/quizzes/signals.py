from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from enpyre_play.scores.tasks import compute_score

from .models import QuizzUserAnswer


@receiver(post_save, sender=QuizzUserAnswer)
def compute_score_on_quizz_user_answer_save(sender, instance, created, **kwargs):
    if created and instance.answer.is_correct and instance.answer.score_amount:
        transaction.on_commit(compute_score.s(instance.user_id, instance.answer.score_amount).delay)
