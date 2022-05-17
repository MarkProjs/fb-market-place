from django.shortcuts import render, get_object_or_404
from web_messaging.models import Message
from .models import Product, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .forms import CommentForm
from django.db.models import Sum, Avg
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .filters import ProductFilter
from django.shortcuts import redirect
from webadminapp.admin import init_groups
from django.core.paginator import Paginator
from .init_data import init_data


# Create your views here.


def home(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'store/home.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'
    paginate_by = 3
    ordering = ['id']

    def get_context_data(self, *args, **kwargs):
        # Initialize Groups, and Admin Users
        init_groups()

        # Initialize Data
        if not User.objects.filter(groups__name='Members').exists():
            init_data()

        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context["new_messages"] = Message.objects.filter(receiver=self.request.user, unread=True).count()
        context['filtered_products'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return ProductFilter(self.request.GET, queryset=queryset).qs


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
        context["avg_rating"] = prod.rate
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
        form.instance.name = self.request.user

        prod = get_object_or_404(Product, id=self.kwargs['pk'])
        if Comment.objects.filter(product=prod).exists():
            sum_rating = Comment.objects.filter(product=prod).aggregate(Sum('rating'))
            count_rating = Comment.objects.filter(product=prod).count() + 1
            avg_rating = (float(sum_rating['rating__sum']) + float(form.instance.rating)) / float(count_rating)
            prod.rate = avg_rating
        else:
            prod.rate = form.instance.rating
        prod.save()
        return super().form_valid(form)


def LikeView(request, pk):
    product = get_object_or_404(Product, id=request.POST.get('product_id'))
    product.likes.add(request.user)
    return HttpResponseRedirect(reverse('product-detail', args=[str(pk)]))


def about(request):
    return render(request, 'store/about.html', {'title': 'About'})


def search_products(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)

        return render(request, 'store/search_products.html', {
            'searched': searched, 'products': products
        })

    else:
        return render(request, 'store/search_products.html', {})


def FlagView(request, pk):
    product = get_object_or_404(Product, id=request.POST.get('product_id'))
    product.flags.add(request.user)
    return HttpResponseRedirect(reverse('product-detail', args=[str(pk)]))


#  Rest API
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductClassSerializer
from django.contrib.auth.decorators import user_passes_test


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, login_url='access-denied')


@api_view(['GET'])
@group_required('Admin_user_group','Admin_item_group','Admin_super_grp')
def api_map(req):
    my_api_urls = {
        'List': 'api/product-list/',
        'Detail': 'api/<int:pk>.product-detail/',
        'Create': 'api/product-new/',
        'Update': 'api/<int:pk>/product-edit/',
        'Delete': 'api/<int:pk>/product-delete/',
    }
    return Response(my_api_urls)


@api_view(['GET'])
@group_required('Admin_user_group','Admin_item_group','Admin_super_grp')
def api_get_all_products(req):
    products = Product.objects.all()
    print(products)
    obj_serializer = ProductClassSerializer(products, many=True)
    return Response(obj_serializer.data)


@api_view(['POST'])
@group_required('Admin_item_group','Admin_super_grp')
def api_create_product(req):
    # if not req.user.is_authenticated():
    #     return redirect('register/')
    obj_serializer = ProductClassSerializer(data=req.data)
    if obj_serializer.is_valid():
        obj_serializer.save()
        return Response(obj_serializer.data, status=status.HTTP_201_CREATED)
    return Response(obj_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_product(pk):
    try:
        product = Product.objects.get(id=pk)
        return product
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@group_required('Admin_user_group','Admin_item_group','Admin_super_grp')
def api_product_detail(req, pk):
    product = get_product(pk)
    obj_serializer = ProductClassSerializer(instance=product)
    return Response(obj_serializer.data)


@api_view(['POST'])
@group_required('Admin_item_group','Admin_super_grp')
def api_product_edit(req, pk):
    product = get_product(pk)
    obj_serializer = ProductClassSerializer(product, data=req.data)
    if obj_serializer.is_valid():
        obj_serializer.save()
        return Response(obj_serializer.data, status=status.HTTP_201_CREATED)
    return Response(obj_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@group_required('Admin_item_group','Admin_super_grp')
def api_product_delete(req, pk):
    this_product = get_product(pk)
    this_product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def go_to_heroku(request):
    return redirect('http://dw-42022-prj-grp6-tat.herokuapp.com')
