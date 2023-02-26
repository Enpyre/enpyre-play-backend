from rest_framework import routers

from .views import (
    GlobalUserScoreViewSet,
    MonthlyUserScoreViewSet,
    ScoreViewSet,
    WeeklyUserScoreViewSet,
    YearlyUserScoreViewSet,
)

router = routers.SimpleRouter()
router.register('weekly', WeeklyUserScoreViewSet, basename='weekly-scores')
router.register('monthly', MonthlyUserScoreViewSet, basename='monthly-scores')
router.register('yearly', YearlyUserScoreViewSet, basename='yearly-scores')
router.register('global', GlobalUserScoreViewSet, basename='global-scores')
router.register('', ScoreViewSet, basename='scores')

urlpatterns = [] + router.urls
