from rest_framework.serializers import ModelSerializer

from enpyre_play.users.serializers import UserSerializer

from .models import Score, UserScore


class UserScoreSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserScore
        fields = ['user', 'total', 'average']
        read_only_fields = ['user', 'total', 'average']


class ScoreSerializer(ModelSerializer):
    scores = UserScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Score
        fields = ['scores']
        read_only_fields = ['scores']
