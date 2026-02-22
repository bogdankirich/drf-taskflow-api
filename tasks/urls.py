from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")
router.register(r"category", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
