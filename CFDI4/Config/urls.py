
from django.urls import path
from .views import * #Group_Add_View,Group_List_View,Group_Update_view,Group_Add_Dynamic_view

urlpatterns = [
    path('list_group/',Group_List_View.as_view(), name='list_group'),
    path('group/add/<str:group>/',Group_Add_View.as_view(), name='Group_Add_View'),
    path('group/<str:group>/edit/<int:pk>/',Group_Edit_View.as_view(), name='edit_group'),
]
