from enpyre_play.serializers import DynamicFieldsModelSerializer
from enpyre_play.users.models import User


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'picture']
