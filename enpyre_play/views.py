from rest_framework.response import Response
from rest_framework.views import APIView


class StatusView(APIView):
    """
    API endpoint that returns the status of the server.
    """

    def get(self, *args, **kwargs):
        return Response({'status': 'ok'})
