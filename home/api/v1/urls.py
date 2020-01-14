from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomTextViewSet,
    HomePageViewSet,
    TableViewSet,
    TestViewSet,
    TestDemoViewSet,
    Testdemo1ViewSet,
    UIViewSet,
    UITestViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
    AppReportView,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("test", TestViewSet)
router.register("testdemo1", Testdemo1ViewSet)
router.register("testdemo", TestDemoViewSet)
router.register("table", TableViewSet)
router.register("ui", UIViewSet)
router.register("uitest", UITestViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("report", AppReportView.as_view(), name="app_report"),
]
