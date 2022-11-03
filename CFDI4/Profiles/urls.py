from django.urls import path, include
from .views import (
    frontpage, 
    ProfileView,
    index,
    ProfileReadMoreListView
)

urlpatterns = [
    path('', index, name='index'),
    path('u/<str:username>/', frontpage, name='frontpage'),
    path('u/<str:usernmae>/Profile/', ProfileView.as_view(), name='ProfileView'),
    path('readMore/', ProfileReadMoreListView.as_view(), name='readmore_view'),
    path('readMore/<str:username>/', ProfileReadMoreListView.as_view(), name='readmore_view'),
    #path('contact/', include('contact_form.urls')),
]