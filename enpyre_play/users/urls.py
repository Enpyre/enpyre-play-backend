from django.urls import path

from .views import UserJWTDetailView

urlpatterns = [path('jwt/', UserJWTDetailView.as_view(), name='current_user_jwt')]
