from rest_framework import status, response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from users.models import User
from users.serializers import UserRegisterSerializer, CurrentUserSerializer


class LoginAPIView(ObtainAuthToken):
    pass


class Signup(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        return user

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token = Token.objects.create(user=user)
        return Response(
            {"token": token.key}, status=status.HTTP_201_CREATED, headers=headers
        )


class CurrentUser(APIView):
    serializer_class = CurrentUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return response.Response({"username": user.username}, status=status.HTTP_200_OK)