import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):

    CHOICES = (
        ('price', 'Price Asc'),
        ('-price', 'Price Desc'),
        ('name', 'Name A-Z'),
        ('-name', 'Name Z-A'),
    )

    ordering = django_filters.ChoiceFilter(
        label='Ordering',
        choices=CHOICES,
        method='filter_by_order'
    )

    def filter_by_order(self, queryset, name, value):
        expression = value
        return queryset.order_by(expression)

    # class Meta:
    #     model = Product
    #     fields = [
    #         'owner',
    #         'type',
    #         'name',
    #         'price',
    #         'description',
    #         'likes',
    #         'size',
    #         'address',
    #         'status',
    #         'flags',
    #     ]




