from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, login_url='access-denied')


# Create your views here.
@group_required('Admin_user_grp')
def admin_dashboard(request):
    context = {
        'title': 'Admin Dashboard',
        'users': User.objects.all()
    }

    return render(request, 'admin_dashboard.html', context)


@group_required('Admin_user_grp')
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
        return redirect('webadminapp-admin-dashboard')
    return render(request, 'admin_confirm_block.html', context)


def error_403(request):
    return render(request, 'access_denied.html')
