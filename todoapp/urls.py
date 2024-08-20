from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.get_todos),
    path('add/', views.add_todo),
    path('delete/<str:pk>/', views.delete_todo),
    path('update/<str:pk>/', views.update_todo),
]
