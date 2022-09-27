from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='userslogin'),
    path('registro/', views.register_view, name='register'),
    path('guardarRegistro/', views.saveregister_view, name='saveregister'),
    path('cerrarSesion/', views.logout_view, name='logout'),
]   