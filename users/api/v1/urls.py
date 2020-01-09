from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DemoViewSet, TeViewSet

router = DefaultRouter()
router.register("demo", DemoViewSet)
router.register("te", TeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
