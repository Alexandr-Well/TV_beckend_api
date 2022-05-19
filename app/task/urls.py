from django.urls import path, include
from rest_framework import routers
from .api import TaskViewSet

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet, basename='Task')

urlpatterns = [
    path('api/', include(router.urls)),
]