
from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    UserProductListView,
    LikeView,
    AddCommentView,
)
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='store-home'),
    path('user/<str:username>/', UserProductListView.as_view(), name='user-products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('about/', views.about, name='store-about'),
    path('like/<int:pk>/', LikeView, name='like-product'),
    path('product/<int:pk>/comment', AddCommentView.as_view(), name='add-comment'),
    path('search_products/', views.search_products, name='search-products'),

]


