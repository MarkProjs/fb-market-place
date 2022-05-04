from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='webadminapp-admin-dashboard'),
    path('confirm_block/<int:pk>', views.confirm_block, name='webadminapp-confirm')
]

