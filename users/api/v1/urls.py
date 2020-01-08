from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DemoViewSet

router = DefaultRouter()
router.register("demo", DemoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
