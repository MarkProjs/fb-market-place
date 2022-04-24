from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def login(request):
    return render(request, 'user_management/login.html', {'title': 'user_management-Login Page'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('store-home')
    else:
        form = UserRegisterForm()
    return render(request, 'user_management/register.html', {'form': form})

# message.debug
# message.info
# message.success
# message.warning
# message.error