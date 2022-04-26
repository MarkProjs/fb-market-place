from django.shortcuts import render
from .models import Product
# Create your views here.


def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store/home.html', context)


def about(request):
    return render(request, 'store/about.html', {'title': 'About'})

