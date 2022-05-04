from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def admin_dashboard(request):
    context = {
        'title': 'Admin Dashboard',
        'users': User.objects.all()
    }
    return render(request, 'admin_dashboard.html', context)

