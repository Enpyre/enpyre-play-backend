from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import URLPattern, URLResolver, include, path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import StatusView

app_urlpatterns: list[URLPattern | URLResolver] = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', include('rest_social_auth.urls_jwt_pair')),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

domain_urlpatterns: list[URLPattern | URLResolver] = [
    path('', StatusView.as_view(), name='status'),
    path('users/', include('enpyre_play.users.urls'), name='users'),
    path('projects/', include('enpyre_play.projects.urls'), name='projects'),
    path('quizzes/', include('enpyre_play.quizzes.urls'), name='quizzes'),
]

urlpatterns = app_urlpatterns + domain_urlpatterns + staticfiles_urlpatterns()
