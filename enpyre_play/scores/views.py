from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from enpyre_play.views import OnlyListModelViewSet

from .models import Score
from .pagination import ScorePaginationClass
from .serializers import ScoreSerializer, UserScoreSerializer


class ScoreViewSet(OnlyListModelViewSet):
    queryset = Score.objects.all().order_by('score_type', 'year', 'month', 'week')
    serializer_class = ScoreSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('score__year', 'score__month', 'score__week')
    pagination_class = ScorePaginationClass


class BaseUserScoreViewSet(OnlyListModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('user__id', 'user__email')
    pagination_class = PageNumberPagination


class WeeklyUserScoreViewSet(BaseUserScoreViewSet):
    def get_queryset(self):
        return Score.get_weekly_score()

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())
        kwargs['exclude_fields'] = ('average',)
        return UserScoreSerializer(*args, **kwargs)


class MonthlyUserScoreViewSet(BaseUserScoreViewSet):
    def get_queryset(self):
        return Score.get_monthly_score()

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())
        kwargs['exclude_fields'] = ('average',)
        return UserScoreSerializer(*args, **kwargs)


class YearlyUserScoreViewSet(BaseUserScoreViewSet):
    def get_queryset(self):
        return Score.get_yearly_score()

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())
        kwargs['exclude_fields'] = ('total',)
        return UserScoreSerializer(*args, **kwargs)


class GlobalUserScoreViewSet(BaseUserScoreViewSet):
    def get_queryset(self):
        return Score.get_global_score()

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())
        kwargs['exclude_fields'] = ('total',)
        return UserScoreSerializer(*args, **kwargs)
