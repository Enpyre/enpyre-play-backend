from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from enpyre_play.scores.tasks import compute_score

from .constants import PROJECT_DEFAULT_SCORE_AMOUNT
from .models import Project


@receiver(post_save, sender=Project)
def compute_score_on_project_save(sender, instance, created, **kwargs):
    if created and instance.public and instance.code:
        transaction.on_commit(compute_score.s(instance.user_id, PROJECT_DEFAULT_SCORE_AMOUNT).delay)
