from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class ProfileView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    model = get_user_model()

    def get_object(self, queryset=None):
        return self.request.user
