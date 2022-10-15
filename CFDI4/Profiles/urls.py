from django.urls import path
from .views import frontpage, ProfileView

urlpatterns = [
    
    path('u/<str:username>/', frontpage, name='frontpage'),
    path('Profile/', ProfileView.as_view(), name='ProfileView'),

]