from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from enpyre_play.users.models import User

from .serializers import UserSerializer


class ProfileView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    model = User

    def get_object(self, queryset=None):
        return self.request.user
