from django.urls import path
from . import views 

urlpatterns = [
    path('', views.hola),
    path('projects/', views.Projects),
    path('tasks/', views.Tasks)
]
