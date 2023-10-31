from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.main, name='main'),
    path('posts/', views.posts, name='posts'),
    path('posts/details/<int:id>', views.details, name='details'),
    ]