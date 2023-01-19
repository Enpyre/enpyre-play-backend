from django.urls import path

from .views import GroupViewSet, UserViewSet

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('groups/', GroupViewSet.as_view({'get': 'list', 'post': 'create'})),
]
