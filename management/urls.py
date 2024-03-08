from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/add/', views.add_room, name='add_room'),
    path('rooms/<int:room_id>/', views.edit_room, name='edit_room'),
    path('rooms/<int:room_id>/delete/', views.delete_room, name='delete_room'),
]
