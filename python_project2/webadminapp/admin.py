from django.contrib import admin
from django.contrib.auth.models import Group, Permission, User


def init_groups():
    # Members Group
    Members, created = Group.objects.get_or_create(name='Members')

    # Admin_user
    Admin_user_grp, created = Group.objects.get_or_create(name='Admin_user_grp')
    if not User.objects.filter(username='user_manager1'):
        user_manager1 = User.objects.create_user(username='user_manager1', password='456')
        Admin_user_grp.user_set.add(user_manager1)

    if not User.objects.filter(username='dan'):
        user_manager = User.objects.create_user(username='dan', password='123')
        Admin_user_grp.user_set.add(user_manager)

    # Missing Warn and Block users
    add_user = Permission.objects.get(codename='add_user')
    delete_user = Permission.objects.get(codename='delete_user')

    user_perms = (add_user, delete_user)
    for perm in user_perms:
        Admin_user_grp.permissions.add(perm)

    # Admin_Items
    Admin_item_grp, created = Group.objects.get_or_create(name='Admin_item_grp')
    if not User.objects.filter(username='item_manager1'):
        item_manager1 = User.objects.create_user(username='item_manager1', password='789')
        Admin_item_grp.user_set.add(item_manager1)

    if not User.objects.filter(username='ken'):
        item_manager = User.objects.create_user(username='ken', password='123')
        Admin_item_grp.user_set.add(item_manager)

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

    if not User.objects.filter(username='rob'):
        super_admin = User.objects.create_user(username='rob', password='123')
        Admin_super_grp.user_set.add(super_admin)

    super_perm = Permission.objects.all()
    for perm in super_perm:
        Admin_super_grp.permissions.add(perm)
