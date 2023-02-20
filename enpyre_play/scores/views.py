from rest_framework import status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Score
from .pagination import ScorePaginationClass
from .serializers import ScoreSerializer


class ScoreViewSet(ModelViewSet):
    queryset = Score.objects.all().order_by('score_type', 'year', 'month', 'week')
    serializer_class = ScoreSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('score__year', 'score__month', 'score__week')
    pagination_class = ScorePaginationClass

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET')

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed('POST')

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')


class CurrentWeeklyScoreView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        weekly_score = Score.get_weekly_score()
        return Response(weekly_score, status=status.HTTP_200_OK)


class CurrentMonthlyScoreView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        monthly_score = Score.get_monthly_score()
        return Response(monthly_score, status=status.HTTP_200_OK)


class CurrentYearlyScoreView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        yearly_score = Score.get_yearly_score()
        return Response(yearly_score, status=status.HTTP_200_OK)


class CurrentGlobalScoreView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        global_score = Score.get_global_score()
        return Response(global_score, status=status.HTTP_200_OK)
