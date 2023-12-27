from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AirplaneViewSet

router = DefaultRouter()
router.register("", AirplaneViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
