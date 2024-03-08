from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='home'),
    
    path('contact/', views.contact, name='contact'),

    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),

    path('login/', views.login_view, name='login'),
    
    path('register/', views.register_view, name='register'),
    
    path('logout/', views.logout_view, name='logout'),
    
    path('profile/', views.profile, name='profile'),
    
    path('rooms/', views.room_list, name='room_list'),
    
    path('room-management/', views.room_management, name='room_management'),
    
    path('staff/', views.staff_list, name='staff_list'),
    
    path('students/add/', views.add_student, name='add_student'),
    
    path('students/', views.student_list, name='student_list'),
    
    path('rooms/', views.room_list, name='room_list'),

    path('book-room/', views.book_room, name='book_room'),
    
    path('search/', views.search_room, name='search_room'),
    
]

