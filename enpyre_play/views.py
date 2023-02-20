from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class StatusView(APIView):
    """
    API endpoint that returns the status of the server.
    """

    def get(self, *args, **kwargs):
        return Response({'status': 'ok'})


class OnlyListModelViewSet(ModelViewSet):
    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET')

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed('POST')

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')
