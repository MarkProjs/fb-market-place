from django.urls import path
from . import views
from .views import AdminListUsers, AdminListItems, AdminDeleteItem, AdminUpdateItem

urlpatterns = [
    path('', views.admin_dashboard, name='webadminapp-admin-dashboard'),
    path('manage_users', AdminListUsers.as_view(), name='webadminapp-manage-users'),
    path('manage_items', AdminListItems.as_view(), name='webadminapp-manage-items'),
    path('manage_items/<int:pk>/delete', AdminDeleteItem.as_view(), name='webadminapp-delete-item'),
    path('manage_items/<int:pk>/update', AdminUpdateItem.as_view(), name='webadminapp-update-item'),
    path('manage_users/<int:pk>/confirm_block', views.confirm_block, name='webadminapp-confirm-block'),
    path('access_denied', views.error_403, name='access-denied')
]
