
from django.urls import path
from .views import Group_Add_View,Group_List_View,Group_Update_view,Group_Add_Dynamic_view

urlpatterns = [
    path('list_group/',Group_List_View.as_view(), name='list_group'),
    path('add_group/',Group_Add_View.as_view(), name='add_group'),
    path('add_group_d/',Group_Add_Dynamic_view.as_view(), name='add_group_d'),
    path('edit_group/<pk>/',Group_Update_view.as_view(), name='edit_group'),



]
