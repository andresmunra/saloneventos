from django.urls import path

from . import views

app_name = 'reservas'

urlpatterns = [
    path('salones/', views.salonesView, name='salones'),
    path('', views.homeView, name='home'),
    path('saveReserva/<salon>', views.saveReservaView, name='saveReserva'),
    path('misReservas/', views.misReservasView, name='misReservas'),
]