from django.db import models

from enpyre_play.users.models import User

from .enums import ScoreTypeSet
from .utils import get_current_month, get_current_week, get_current_year


class Score(models.Model):
    score_type = models.CharField(max_length=10)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)
    week = models.IntegerField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['score_type', '-year', 'month', 'week'], name='score_type_idx'),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['score_type', 'year', 'month', 'week'], name='unique_score'
            )
        ]
        ordering = ['score_type', '-year', 'month', 'week']

    @classmethod
    def build(cls, score_type: ScoreTypeSet):
        params = {
            'score_type': score_type,
            'year': None,
            'month': None,
            'week': None,
        }
        if score_type in [ScoreTypeSet.WEEKLY, ScoreTypeSet.MONTHLY, ScoreTypeSet.YEARLY]:
            params['year'] = get_current_year()
        if score_type in [ScoreTypeSet.MONTHLY, ScoreTypeSet.YEARLY]:
            params['month'] = get_current_month()
        if score_type == ScoreTypeSet.WEEKLY:
            params['week'] = get_current_week()
        return cls.objects.get_or_create(**params)[0]

    @classmethod
    def get_global_score(cls):
        global_score = cls.build(ScoreTypeSet.GLOBAL)
        user_scores = (
            UserScore.objects.filter(score=global_score)
            .order_by('-average')
            .values('user__username', 'average')
            .values_list('user__username', 'average')
        )
        return list(user_scores)

    @classmethod
    def get_weekly_score(cls):
        weekly_score = cls.build(ScoreTypeSet.WEEKLY)
        user_scores = (
            UserScore.objects.filter(score=weekly_score)
            .order_by('-total')
            .values('user__username', 'total')
            .values_list('user__username', 'total')
        )
        return list(user_scores)

    @classmethod
    def get_monthly_score(cls):
        monthly_score = cls.build(ScoreTypeSet.MONTHLY)
        user_scores = (
            UserScore.objects.filter(score=monthly_score)
            .order_by('-total')
            .values('user__username', 'total')
            .values_list('user__username', 'total')
        )
        return list(user_scores)

    @classmethod
    def get_yearly_score(cls):
        yearly_score = cls.build(ScoreTypeSet.YEARLY)
        user_scores = (
            UserScore.objects.filter(score=yearly_score)
            .order_by('-average')
            .values('user__username', 'average')
            .values_list('user__username', 'average')
        )
        return list(user_scores)


class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    average = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    average_count = models.IntegerField(default=0)

    score = models.ForeignKey(Score, on_delete=models.CASCADE, related_name='user_scores')

    class Meta:
        indexes = [
            models.Index(fields=['-total'], name='user_total_idx'),
            models.Index(fields=['-average'], name='user_average_idx'),
        ]
        ordering = ['-total']

    @classmethod
    def build(cls, user_id: int, score):
        user_score, _ = cls.objects.get_or_create(user__id=user_id, score=score)
        return user_score

    def compute(self, score_amount):
        self.total += score_amount
        self.average_count += 1
        self.average = self.total / self.average_count
        self.save()
