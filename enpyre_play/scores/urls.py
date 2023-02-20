from django.urls import path
from rest_framework import routers

from .views import (
    CurrentGlobalScoreView,
    CurrentMonthlyScoreView,
    CurrentWeeklyScoreView,
    CurrentYearlyScoreView,
    ScoreViewSet,
)

router = routers.SimpleRouter()
router.register('', ScoreViewSet, basename='scores')


urlpatterns = [
    path('weekly/', CurrentWeeklyScoreView.as_view(), name='weekly'),
    path('monthly/', CurrentMonthlyScoreView.as_view(), name='monthly'),
    path('yearly/', CurrentYearlyScoreView.as_view(), name='yearly'),
    path('global/', CurrentGlobalScoreView.as_view(), name='global'),
] + router.urls
