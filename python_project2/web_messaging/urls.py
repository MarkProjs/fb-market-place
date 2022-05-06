from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.MessageView.as_view(), name='web_messaging_send'),
]
