from rest_framework.serializers import ModelSerializer

from enpyre_play.serializers import DynamicFieldsModelSerializer
from enpyre_play.users.serializers import UserSerializer

from .models import Score, UserScore


class UserScoreSerializer(DynamicFieldsModelSerializer):
    user = UserSerializer(read_only=True, exclude_fields=('email',))

    class Meta:
        model = UserScore
        fields = ['user', 'total', 'average']
        read_only_fields = ['user', 'total', 'average']


class ScoreSerializer(ModelSerializer):
    user_scores = UserScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Score
        fields = ['score_type', 'year', 'month', 'week', 'user_scores']
        read_only_fields = ['score_type', 'year', 'month', 'week', 'user_scores']
