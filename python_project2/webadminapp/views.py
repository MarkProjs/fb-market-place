from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView


# Create your views here.
def admin_dashboard(request):
    context = {
        'title': 'Admin Dashboard',
        'users': User.objects.all()
    }

    return render(request, 'admin_dashboard.html', context)


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
