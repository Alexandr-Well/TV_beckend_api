import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf
from braces.views import CsrfExemptMixin


class UserViewSet(viewsets.ModelViewSet):
    """API для получения юзера"""
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.query_params.get('date'):
            return User.objects.filter(username=self.request.query_params.get('name'))
        return User.objects.all()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginView(CsrfExemptMixin, APIView):
    """API для логина"""
    authentication_classes = []

    def post(self, request, format=None):
        data = request.data
        response = Response()
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value=data["access"],
                    expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite='None'
                )
                csrf.get_token(request)
                response.data = {"Success": "Login successfully", "data": data}

                return response
            else:
                return Response({"No active": "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid": "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)


class UserView(CsrfExemptMixin, APIView):
    """API для получения юзера"""
    authentication_classes = []

    def get(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(pk=payload['user_id']).first()

        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(CsrfExemptMixin, APIView):
    """API для выхода из под аккаунта"""
    authentication_classes = []

    def post(self, request):
        response = Response()
        response.delete_cookie('access_token')
        response.data = {
            'message': 'success'
        }
        return response
