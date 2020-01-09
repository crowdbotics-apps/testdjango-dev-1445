from rest_framework import authentication
from users.models import Demo, Te
from .serializers import DemoSerializer, TeSerializer
from rest_framework import viewsets


class DemoViewSet(viewsets.ModelViewSet):
    serializer_class = DemoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Demo.objects.all()


class TeViewSet(viewsets.ModelViewSet):
    serializer_class = TeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Te.objects.all()
