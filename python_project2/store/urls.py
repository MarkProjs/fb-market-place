
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
    FlagView,
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
    path('flag/<int:pk>/', FlagView, name='flag-product'),
    path('api/', views.api_map, name='api_map'),
    path('api/product-list/', views.api_get_all_products, name='api_product_list'),
    path('api/product-new/', views.api_create_product, name='api_product_new'),
    path('api/<int:pk>/product-detail', views.api_product_detail, name='api_product_detail'),
    path('api/<int:pk>/product-edit', views.api_product_edit, name='api_product_edit'),
    path('api/<int:pk>/product-delete', views.api_product_delete, name='api_product_delete'),
    path('heroku', views.go_to_heroku, name='heroku'),
]



