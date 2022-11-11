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

    Techs_ListView,
    Techs_Edit_View,
    Techs_Delete_View,

    Socials_ListView,
    Socials_Edit_View,
    Socials_Delete_View,

    Work_Images_List_View,
    work_Images_Edit_View,
    Work_Images_Delete_View,
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
    path('techs/', Techs_ListView.as_view(), name='techs_view'),
    path('techs/edit/',Techs_Edit_View.as_view(), name='techs_edit_view'),
    path('techs/delete/<int:pk>/',Techs_Delete_View.as_view(), name='techs_delete_view'),
    path('socials/', Socials_ListView.as_view(), name='socials_view'),
    path('socials/edit/',Socials_Edit_View.as_view(), name='socials_edit_view'),
    path('socials/delete/<int:pk>/',Socials_Delete_View.as_view(), name='socials_delete_view'),
    
    path('workimages/', Work_Images_List_View.as_view(), name='workimages_view'),
    path('workimages/edit/',work_Images_Edit_View.as_view(), name='workimages_edit_view'),
    path('workimages/delete/<int:pk>/',Work_Images_Delete_View.as_view(), name='workimages_delete_view'),
    
]