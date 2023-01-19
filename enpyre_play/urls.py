from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path

urlpatterns: list[URLPattern | URLResolver] = [
    path('admin/', admin.site.urls, name='admin'),
    path('users/', include('enpyre_play.user.urls'), name='users'),
]
