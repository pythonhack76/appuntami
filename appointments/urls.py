from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_appointments, name='home_appointments'),
    path('create/', views.create_appointment, name='create_appointment'),
    path('list/', views.list_appointments, name='list_appointments'),
    path('<int:id>/', views.appointment_detail, name='appointment_detail'),  # Aggiungi questa riga
    path('<int:id>/update/', views.update_appointment, name='update_appointment'),  # Aggiungi questa riga
]
