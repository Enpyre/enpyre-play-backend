from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Project, ProjectSolution
from .serializers import ProjectSerializer, ProjectSolutionSerializer


class ProjectSearchFilter(SearchFilter):
    def filter_queryset(self, request, queryset: QuerySet[Project], view):
        if link := request.query_params.get('link'):
            if not link.endswith('/'):
                link += '/'
            _queryset = Project.objects.filter(link=link, shared=True)
            _queryset |= Project.objects.filter(link=link, user=request.user)
            return _queryset.distinct()
        return super().filter_queryset(request, queryset, view)


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    lookup_field = 'id'
    filter_backends = [ProjectSearchFilter]
    search_fields = ['title', 'description', 'code', 'link', 'user_id']
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        user_projects = Project.objects.filter(user=self.request.user)
        public_projects = Project.objects.filter(public=True).exclude(user=self.request.user)
        projects = user_projects | public_projects
        return projects.order_by('-updated_at')

    def retrieve(self, request, *args, **kwargs):
        project = self.get_object()
        if project.public or project.user == request.user:
            return super().retrieve(request, *args, **kwargs)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ProjectSulutionViewSet(RetrieveModelMixin, GenericAPIView):
    serializer_class = ProjectSolutionSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = ProjectSolution.objects.all()
    lookup_field = 'project_id'

    def retrieve(self, request, *args, **kwargs):
        project_id = kwargs['project_id']

        project_solution = get_object_or_404(
            ProjectSolution, project_id=project_id, user=request.user
        )
        serializer = self.serializer_class(project_solution)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
