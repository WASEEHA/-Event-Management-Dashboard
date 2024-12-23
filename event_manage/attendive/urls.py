from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendee_list, name='attendee_list'),
    path('create/', views.attendee_create, name='attendee_create'),
    path('edit/<int:pk>/', views.attendee_edit, name='attendee_edit'),
    path('delete/<int:pk>/', views.attendee_delete, name='attendee_delete'),
]