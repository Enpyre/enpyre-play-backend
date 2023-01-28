from rest_framework.serializers import ModelSerializer

from enpyre_play.users.serializers import UserSerializer

from .models import Project


class ProjectSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'code', 'link', 'shared', 'public', 'user']
