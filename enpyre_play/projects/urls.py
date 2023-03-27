from django.urls import path
from rest_framework import routers

from .views import ProjectSulutionViewSet, ProjectViewSet

router = routers.SimpleRouter()
router.register('', ProjectViewSet, basename='projects')

urlpatterns = [
    path(
        '<int:project_id>/solutions/mine',
        ProjectSulutionViewSet.as_view(),
    ),
] + router.urls
