from django.urls import path, include
from .views import frontpage, ProfileView,index

urlpatterns = [
    path('', index, name='index'),
    path('u/<str:username>/', frontpage, name='frontpage'),
    path('u/<str:usernmae>/Profile/', ProfileView.as_view(), name='ProfileView'),
    #path('contact/', include('contact_form.urls')),
]