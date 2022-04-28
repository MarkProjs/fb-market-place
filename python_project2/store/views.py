from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.


def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store/home.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description']


def about(request):
    return render(request, 'store/about.html', {'title': 'About'})

