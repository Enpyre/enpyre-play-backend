from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import URLPattern, URLResolver, include, path

from .views import StatusView

urlpatterns: list[URLPattern | URLResolver] = [
    path('', StatusView.as_view(), name='status'),
    path('admin/', admin.site.urls, name='admin'),
    path('users/', include('enpyre_play.user.urls'), name='users'),
] + staticfiles_urlpatterns()
