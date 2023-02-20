from django.db import models, transaction
from django.db.models.query_utils import Q

from enpyre_play.decorators import durable
from enpyre_play.models import BaseModel
from enpyre_play.users.models import User

from .enums import ScoreTypeSet
from .utils import get_current_month, get_current_week, get_current_year


class Score(BaseModel):
    score_type = models.CharField(max_length=10)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)
    week = models.IntegerField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['score_type', '-year', 'month', 'week'], name='score_type_idx'),
        ]
        constraints = [
            models.CheckConstraint(
                check=(
                    Q(score_type__in=list(ScoreTypeSet))
                    & (
                        Q(
                            score_type=ScoreTypeSet.WEEKLY,
                            year__isnull=False,
                            month__isnull=False,
                            week__isnull=False,
                        )
                        | Q(
                            score_type=ScoreTypeSet.MONTHLY,
                            year__isnull=False,
                            month__isnull=False,
                            week__isnull=True,
                        )
                        | Q(
                            score_type=ScoreTypeSet.YEARLY,
                            year__isnull=False,
                            month__isnull=True,
                            week__isnull=True,
                        )
                        | Q(
                            score_type=ScoreTypeSet.GLOBAL,
                            year__isnull=True,
                            month__isnull=True,
                            week__isnull=True,
                        )
                    )
                ),
                name='valid_score',
            ),
            models.UniqueConstraint(
                fields=['score_type', 'year', 'month', 'week'],
                name='unique_score',
                deferrable=models.Deferrable.DEFERRED,
            ),
        ]
        ordering = ['score_type', '-year', 'month', 'week']

    @classmethod
    @durable
    def build(cls, score_type: ScoreTypeSet):
        with transaction.atomic(durable=True):
            params = {
                'score_type': score_type,
                'year': None,
                'month': None,
                'week': None,
            }
            if score_type in [ScoreTypeSet.WEEKLY, ScoreTypeSet.MONTHLY, ScoreTypeSet.YEARLY]:
                params['year'] = get_current_year()
            if score_type in [ScoreTypeSet.WEEKLY, ScoreTypeSet.MONTHLY]:
                params['month'] = get_current_month()
            if score_type == ScoreTypeSet.WEEKLY:
                params['week'] = get_current_week()
            return cls.objects.get_or_create(**params)[0]

    @classmethod
    def get_weekly_score(cls):
        weekly_score = cls.build(ScoreTypeSet.WEEKLY)
        return UserScore.objects.filter(score=weekly_score).order_by('-total')

    @classmethod
    def get_monthly_score(cls):
        monthly_score = cls.build(ScoreTypeSet.MONTHLY)
        return UserScore.objects.filter(score=monthly_score).order_by('-total')

    @classmethod
    def get_yearly_score(cls):
        yearly_score = cls.build(ScoreTypeSet.YEARLY)
        user_scores = UserScore.objects.filter(score=yearly_score).order_by('-average')
        return user_scores

    @classmethod
    def get_global_score(cls):
        global_score = cls.build(ScoreTypeSet.GLOBAL)
        return UserScore.objects.filter(score=global_score).order_by('-average')


class UserScore(BaseModel):
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
    @durable
    def build(cls, user_id: int, score: Score):
        with transaction.atomic(durable=True):
            user = User.objects.get(id=user_id)
            user_score, _ = cls.objects.get_or_create(user=user, score=score)
            return user_score

    @durable
    def compute(self, score_amount):
        with transaction.atomic(durable=True):
            self.total += score_amount
            self.average_count += 1
            self.average = self.total / self.average_count
            self.save()
