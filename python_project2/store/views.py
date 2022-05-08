
from django.shortcuts import render, get_object_or_404
from .models import Product, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .forms import CommentForm
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

    def get_context_data(self, *args, **kwargs):
        # product_menu=Product.object.all()
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        prod = get_object_or_404(Product, id=self.kwargs['pk'])
        total_likes = prod.total_likes()
        total_flags = prod.total_flags()
        context["total_likes"] = total_likes
        context["total_flags"] = total_flags
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['type', 'name', 'address', 'status', 'price', 'size', 'description', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['type', 'name', 'address', 'status', 'price', 'size', 'description', 'image']

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


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'store/add_comment.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)


def LikeView(request, pk):
    product = get_object_or_404(Product, id=request.POST.get('product_id'))
    product .likes.add(request.user)
    return HttpResponseRedirect(reverse('product-detail', args=[str(pk)]))


def about(request):
    return render(request, 'store/about.html', {'title': 'About'})


def search_products(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)

        return render(request, 'store/search_products.html', {'searched': searched, 'products': products})

    else:
        return render(request, 'store/search_products.html', {})


def FlagView(request, pk):
    product = get_object_or_404(Product, id=request.POST.get('product_id'))
    product .flags.add(request.user)
    return HttpResponseRedirect(reverse('product-detail', args=[str(pk)]))
