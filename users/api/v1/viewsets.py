from rest_framework import authentication
from users.models import Demo
from .serializers import DemoSerializer
from rest_framework import viewsets


class DemoViewSet(viewsets.ModelViewSet):
    serializer_class = DemoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Demo.objects.all()
