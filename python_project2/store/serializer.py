from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductClassSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
