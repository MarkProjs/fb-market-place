from django.contrib import admin
from django.contrib.auth.models import Group, Permission, User

# Register your models here.
Members, created = Group.objects.get_or_create(name='Members')

Admin_user_grp, created = Group.objects.get_or_create(name='Admin_user_grp')
user_manager1, created = User.objects.get_or_create(username='user_manager1', password='456')
Admin_user_grp.user_set.add(user_manager1)

Admin_item_grp, created = Group.objects.get_or_create(name='Admin_item_grp')
item_manager1, created = User.objects.get_or_create(username='item_manager1', password='789')
Admin_item_grp.user_set.add(item_manager1)

Admin_super_grp, created = Group.objects.get_or_create(name='Admin_super_grp')
if not User.objects.filter(username='nasr'):
    nasr = User.objects.create_superuser(username='nasr', password='123')
    Admin_super_grp.user_set.add(nasr)

