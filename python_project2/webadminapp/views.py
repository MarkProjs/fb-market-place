from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def admin_dashboard(request):
    context = {
        'title': 'Admin Dashboard',
        'users': User.objects.all()
    }

    return render(request, 'admin_dashboard.html', context)


def confirm_block(request):
    context = {
        'user': user
    }

    return render(request, 'admin_confirm_block.html', context)