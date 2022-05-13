from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from store.models import Product
from web_messaging.models import Message
from django.views.generic import (
    ListView,
    DeleteView,
    UpdateView
)


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, login_url='access-denied')


@group_required('Admin_user_grp', 'Admin_item_grp', 'Admin_super_grp')
def admin_dashboard(request):
    context = {
        'title': 'Admin Dashboard',
    }
    return render(request, 'admin_dashboard.html', context)


class AdminListUsers(ListView):
    queryset = User.objects.filter(groups__name='Members')
    template_name = 'admin_manage_users.html'
    paginate_by = 3
    context_object_name = 'users'

    def get_context_data(self, *args, **kwargs):
        context = super(AdminListUsers, self).get_context_data(*args, **kwargs)
        context["title"] = 'Admin Manage Users'
        return context

    @method_decorator(group_required('Admin_user_grp', 'Admin_super_grp'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AdminListItems(ListView):
    model = Product
    template_name = 'admin_manage_items.html'
    context_object_name = 'products'
    paginate_by = 3
    ordering = ['id']

    def get_context_data(self, *args, **kwargs):
        context = super(AdminListItems, self).get_context_data(*args, **kwargs)
        context["title"] = 'Admin Manage Items'
        return context

    @method_decorator(group_required('Admin_item_grp', 'Admin_super_grp'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AdminDeleteItem(DeleteView):
    model = Product
    success_url = '/webadminapp/manage_items'

    @method_decorator(group_required('Admin_item_grp', 'Admin_super_grp'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AdminUpdateItem(UpdateView):
    model = Product
    fields = ['type', 'name', 'address', 'status', 'price', 'size', 'description', 'image']
    success_url = '/webadminapp/manage_items'

    def form_valid(self, form):
        return super().form_valid(form)

    @method_decorator(group_required('Admin_item_grp', 'Admin_super_grp'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@group_required('Admin_user_grp', 'Admin_super_grp')
def confirm_block(request, pk):
    context = {
        'user': User.objects.get(id=pk)
    }
    if request.method == "POST":
        target = context['user']
        data = request.POST
        action = data.get("target")
        if action == "block":
            target.is_active = False
        elif action == "unblock":
            target.is_active = True
        target.save()
        return redirect('webadminapp-manage-users')

    if context['user'].groups.filter(name="Members").exists():
        return render(request, 'admin_confirm_block.html', context)
    else:
        return redirect('access-denied')


@group_required('Admin_user_grp', 'Admin_super_grp')
def confirm_warn(request, pk):
    context = {
        'user': User.objects.get(id=pk)
    }
    if request.method == "POST":
        receiver_name = context['user']
        receiver = User.objects.get(username=receiver_name)
        msg_body = 'This is an automated message,\nAn Admin has issued a Warning\nFurther Warnings may lead to ' \
                   'deactivating your account'
        Message.objects.create(sender=request.user, receiver=receiver, message=msg_body)
        return redirect('webadminapp-manage-users')

    if context['user'].groups.filter(name="Members").exists():
        return render(request, 'admin_confirm_warn.html', context)
    else:
        return redirect('access-denied')


def error_403(request):
    return render(request, 'access_denied.html')

