from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import SignUpSerializer


login = obtain_auth_token


class SignUpView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serialized_data = SignUpSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()

            return Response(data={'message': f'Welcome {request.user.username}!'}, status=201)


class LogOut(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        request.user.auth_token.delete()

        return Response(data={'message': f'Bye {request.user.username}!'}, status=200)


class AllUsers(APIView):
    permission_classes = (IsAdminUser, )

    def get(self, request):
        data = User.objects.values_list('username', flat=True)

        return Response({"data": data}, status=200)
