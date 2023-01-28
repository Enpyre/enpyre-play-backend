from django.db.models import QuerySet
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Project
from .serializers import ProjectSerializer


class ProjectSearchFilter(SearchFilter):
    def filter_queryset(self, request, queryset: QuerySet[Project], view):
        _queryset = queryset
        if link := request.query_params.get('link'):
            _queryset = Project.objects.filter(link=link, shared=True).get_queryset() | queryset
            _queryset = _queryset.distinct()
        return super().filter_queryset(request, _queryset, view)


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    lookup_field = 'id'
    filter_backends = [ProjectSearchFilter]
    search_fields = ['title', 'description', 'code', 'link', 'user_id']

    def get_queryset(self):
        user_projects = Project.objects.filter(user=self.request.user)
        public_projects = Project.objects.filter(public=True)
        return user_projects | public_projects

    def retrieve(self, request, *args, **kwargs):
        project = self.get_object()
        if project.public or project.user == request.user:
            return super().retrieve(request, *args, **kwargs)
        return Response(status=status.HTTP_404_NOT_FOUND)
