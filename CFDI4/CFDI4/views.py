
from rest_framework.permissions import AllowAny
from rest_framework import views
from rest_framework.response import Response
from . import serializers

from django.contrib.auth import login, logout,authenticate
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status

from django.shortcuts import redirect,render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm

class SignUpView(generic.CreateView):
    # form_class = UserCreationForm
    form_class = SignupForm
    success_url = reverse_lazy("index")
    template_name = "Profiles/signup.html"
    
#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer




class LoginPageView(generic.View):
    template_name = 'Profiles/login.html'
    form_class = AuthenticationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        message =''
        
        return render(request,self.template_name, {
            'form':form,
            'message':message
        })
    def post(self, request, *args, **kwargs):
        form = self.form_class(request=request, data=request.POST)
        
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('index')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})

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




