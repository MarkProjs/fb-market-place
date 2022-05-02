from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
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
    paginate_by = 3


class UserProductListView(ListView):
    model = Product
    template_name = 'store/user_products.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(owner=user)


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.owner:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.owner:
            return True
        return False


def about(request):
    return render(request, 'store/about.html', {'title': 'About'})

