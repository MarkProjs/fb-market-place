from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='user_management-login'),
    path('register/', views.register, name='user_management-register'),
]
