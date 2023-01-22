from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import URLPattern, URLResolver, include, path

from .views import StatusView

urlpatterns: list[URLPattern | URLResolver] = [
    path('', StatusView.as_view(), name='status'),
    path('admin/', admin.site.urls, name='admin'),
    path('users/', include('enpyre_play.users.urls'), name='users'),
    path('login/', include('rest_social_auth.urls_jwt_pair')),
] + staticfiles_urlpatterns()
