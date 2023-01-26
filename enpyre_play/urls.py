from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import URLPattern, URLResolver, include, path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import StatusView

urlpatterns: list[URLPattern | URLResolver] = [
    path('', StatusView.as_view(), name='status'),
    path('admin/', admin.site.urls, name='admin'),
    path('users/', include('enpyre_play.users.urls'), name='users'),
    path('login/', include('rest_social_auth.urls_jwt_pair')),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + staticfiles_urlpatterns()
