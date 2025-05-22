from django.urls import path
from . import views

urlpatterns = [
    path('', views.transport_form_list, name='transport_form_list'),
    path('nuevo/', views.transport_form_create, name='transport_form_create'),
    path('editar/<int:pk>/', views.transport_form_edit, name='transport_form_edit'),
    path('eliminar/<int:pk>/', views.transport_form_delete, name='transport_form_delete'),
]