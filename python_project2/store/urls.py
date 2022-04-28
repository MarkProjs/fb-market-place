from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='store-home'),
    path('product/<pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('about/', views.about, name='store-about'),
]


