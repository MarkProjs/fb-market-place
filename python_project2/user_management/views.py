from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import Group, User

# Create your views here.
def register(request):
    g = Group.objects.get(name='Members')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=f'{username}')
            g.user_set.add(user)
            messages.success(request, f'Account has been created! You can now log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user_management/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'user_management/profile.html')