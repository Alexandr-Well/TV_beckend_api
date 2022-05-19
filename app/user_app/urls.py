from django.urls import path, include
from rest_framework import routers
from .api import UserViewSet, LoginView, UserView, LogoutView

router = routers.SimpleRouter()
router.register(r'profiles', UserViewSet, basename='Profile')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', LoginView.as_view(), name="login"),
    path('api/user/', UserView.as_view(), name="user"),
    path('api/logout/', LogoutView.as_view(), name="logout"),
]
