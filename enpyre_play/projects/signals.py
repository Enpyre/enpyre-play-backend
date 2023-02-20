from django.db.models.signals import post_save
from django.dispatch import receiver

from enpyre_play.scores.tasks import compute_score

from .constants import PROJECT_DEFAULT_SCORE_AMOUNT
from .models import Project


@receiver(post_save, sender=Project)
def compute_score_on_quizz_user_answer_save(sender, instance, created, **kwargs):
    if created and instance.public and instance.code:
        compute_score.delay(instance.user_id, PROJECT_DEFAULT_SCORE_AMOUNT)
