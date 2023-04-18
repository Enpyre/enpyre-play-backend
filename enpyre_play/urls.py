from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import URLPattern, URLResolver, include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import StatusView

app_urlpatterns: list[URLPattern | URLResolver] = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', include('rest_social_auth.urls_jwt_pair')),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

domain_urlpatterns: list[URLPattern | URLResolver] = [
    path('', StatusView.as_view(), name='status'),
    path('users/', include('enpyre_play.users.urls'), name='users'),
    path('projects/', include('enpyre_play.projects.urls'), name='projects'),
    path('quizzes/', include('enpyre_play.quizzes.urls'), name='quizzes'),
    path('scores/', include('enpyre_play.scores.urls'), name='scores'),
]

urlpatterns = app_urlpatterns + domain_urlpatterns + staticfiles_urlpatterns()
