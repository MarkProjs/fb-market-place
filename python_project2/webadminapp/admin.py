from django.contrib import admin
from django.contrib.auth.models import Group, Permission, User

# Members Group
Members, created = Group.objects.get_or_create(name='Members')

# Admin_user
Admin_user_grp, created = Group.objects.get_or_create(name='Admin_user_grp')
user_manager1, created = User.objects.get_or_create(username='user_manager1', password='456')
Admin_user_grp.user_set.add(user_manager1)

# Missing Warn and Block users
add_user = Permission.objects.get(codename='add_user')
delete_user = Permission.objects.get(codename='delete_user')

user_perms = (add_user, delete_user)
for perm in user_perms:
    Admin_user_grp.permissions.add(perm)

# Admin_Items
Admin_item_grp, created = Group.objects.get_or_create(name='Admin_item_grp')
item_manager1, created = User.objects.get_or_create(username='item_manager1', password='789')
Admin_item_grp.user_set.add(item_manager1)

add_product = Permission.objects.get(codename='add_product')
change_product = Permission.objects.get(codename='change_product')
delete_product = Permission.objects.get(codename='delete_product')

item_perms = (add_product, change_product, delete_product)
for perm in item_perms:
    Admin_item_grp.permissions.add(perm)

# Super Users
Admin_super_grp, created = Group.objects.get_or_create(name='Admin_super_grp')
if not User.objects.filter(username='nasr'):
    nasr = User.objects.create_superuser(username='nasr', password='123')
    Admin_super_grp.user_set.add(nasr)

super_perm = Permission.objects.all()
for perm in super_perm:
    Admin_super_grp.permissions.add(perm)
