from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='webadminapp-admin-dashboard'),
    path('manage_users', views.admin_manage_users, name='webadminapp-manage-users'),
    path('manage_items', views.admin_manage_items, name='webadminapp-manage-items'),
    path('confirm_block/<int:pk>', views.confirm_block, name='webadminapp-confirm'),
    path('access_denied', views.error_403, name='access-denied')
]

