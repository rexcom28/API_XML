
from rest_framework.permissions import AllowAny
from rest_framework import views
from rest_framework.response import Response
from . import serializers
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status


from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.parsers import MultiPartParser, FileUploadParser


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    parser_class = (FileUploadParser,)
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer
        
class LoginView(views.APIView):
# This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        #serializer = serializers.LoginSerializer(data=self.request.data,context={ 'request': self.request })
        serializer = serializers.LoginSerializer(data=self.request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)

class LogoutView(LoginRequiredMixin, views.APIView):
    def post(self, request, format=None, *args, **kwargs):
        logout(request)
        #return Response(None, status=status.HTTP_204_NO_CONTENT)
        return redirect('login')
class ProfileView(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user




