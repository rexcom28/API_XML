from django.urls import path, include
from .views import (
    frontpage, 
    ProfileView,
    index,
    ProfileReadMoreListView,
    ProfileReadMoreEditView,
    Contact_ListView,
    Contact_is_readed_view,
    ProfileReadMore_Delete_View,
)

urlpatterns = [
    path('', index, name='index'),
    path('u/<str:username>/', frontpage, name='frontpage'),
    path('u/<str:usernmae>/Profile/', ProfileView.as_view(), name='ProfileView'),
    path('contactList/', Contact_ListView.as_view(),name='contact_list_view'),
    path('contactList/is_read/',Contact_is_readed_view.as_view() ,name='contact_is_readed_view'),
    path('readMore/delete/<int:pk>/',ProfileReadMore_Delete_View.as_view(), name='readmore_delete_view'),
    path('readMore/edit/',ProfileReadMoreEditView.as_view(), name='readmore_edit_view'),
    path('readMore/', ProfileReadMoreListView.as_view(), name='readmore_view'),
    path('readMore/<str:username>/', ProfileReadMoreListView.as_view(), name='readmore_view'),
    
    #path('contact/', include('contact_form.urls')),
]