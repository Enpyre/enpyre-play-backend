from uuid import uuid4

from rest_framework.serializers import ModelSerializer

from enpyre_play.envs import PROJECT_LINK_BASE_URL
from enpyre_play.users.serializers import UserSerializer

from .models import Project


class ProjectSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'code',
            'link',
            'shared',
            'public',
            'user',
            'updated_at',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'link',
            'user',
            'updated_at',
            'created_at',
        ]

    def create(self, validated_data):
        validated_data['link'] = f'{PROJECT_LINK_BASE_URL}{uuid4()}'
        request = self.context.get('request')
        validated_data['user_id'] = request.user.id
        return super().create(validated_data)
