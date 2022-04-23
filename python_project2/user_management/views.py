from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'user_management/login.html', {'title': 'user_management-Login Page'})

def register(request):
    return render(request, 'user_management/register.html', {'title': 'user_management-Register Page'})