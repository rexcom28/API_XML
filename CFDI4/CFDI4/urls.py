"""CFDI4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import LoginView, LogoutView, RegisterUserAPIView, SignUpView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import  views as auth_views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('register/', RegisterUserAPIView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('Cats/', include('Cats.urls')),
    path('', include('Profiles.urls')),
    path('', include('Config.urls')),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    
    path('login2/',auth_views.LoginView.as_view(template_name = 'Profiles/login.html'), name='login2'),
    path('logout2/', auth_views.LogoutView.as_view(), name='logout2'),
    path("accounts/", include("django.contrib.auth.urls")),
]
if settings.DEBUG: #DEV only
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
