from rest_framework import viewsets
from rest_framework import authentication
from .serializers import (
    CustomTextSerializer,
    DummySerializer,
    HomePageSerializer,
    TableSerializer,
    TestSerializer,
    TestDSerializer,
    TestDataSerializer,
    TestDemoSerializer,
    Testdemo1Serializer,
    TestModelSerializer,
    UISerializer,
    UITestSerializer,
)
import json

from django import apps
from django.core.management import call_command
from .permissions import CrowboticsExclusive

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from home.api.v1.serializers import (
    SignupSerializer,
    CustomTextSerializer,
    HomePageSerializer,
    UserSerializer,
)
from home.models import (
    CustomText,
    Dummy,
    HomePage,
    Table,
    Test,
    TestD,
    TestData,
    TestDemo,
    Testdemo1,
    TestModel,
    UI,
    UITest,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class CustomTextViewSet(ModelViewSet):
    serializer_class = CustomTextSerializer
    queryset = CustomText.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class HomePageViewSet(ModelViewSet):
    serializer_class = HomePageSerializer
    queryset = HomePage.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class AppReportView(APIView):
    """
    DO NOT REMOVE THIS CODE SNIPPET, YOUR DASHBOARD MAY NOT REFLECT THE CORRECT
    RESOURCES IN YOUR APP.
    """

    permission_classes = [CrowboticsExclusive]

    def _get_models(self):
        project_models = apps.apps.get_models(
            include_auto_created=True, include_swapped=True
        )
        parsed_data = [
            str(model).split(".")[-1].replace("'", "").strip(">")
            for model in project_models
        ]
        return parsed_data

    def _get_urls(self):
        parsed_data = json.loads(call_command("show_urls", format="json"))
        return parsed_data

    def get(self, request):
        return Response(
            {"models": self._get_models(), "urls": self._get_urls()},
            status=status.HTTP_200_OK,
        )


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Test.objects.all()


class Testdemo1ViewSet(viewsets.ModelViewSet):
    serializer_class = Testdemo1Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Testdemo1.objects.all()


class TestDemoViewSet(viewsets.ModelViewSet):
    serializer_class = TestDemoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TestDemo.objects.all()


class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Table.objects.all()


class UIViewSet(viewsets.ModelViewSet):
    serializer_class = UISerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = UI.objects.all()


class UITestViewSet(viewsets.ModelViewSet):
    serializer_class = UITestSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = UITest.objects.all()


class TestDataViewSet(viewsets.ModelViewSet):
    serializer_class = TestDataSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TestData.objects.all()


class TestModelViewSet(viewsets.ModelViewSet):
    serializer_class = TestModelSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TestModel.objects.all()


class DummyViewSet(viewsets.ModelViewSet):
    serializer_class = DummySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Dummy.objects.all()


class TestDViewSet(viewsets.ModelViewSet):
    serializer_class = TestDSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TestD.objects.all()
