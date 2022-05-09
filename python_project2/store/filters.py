import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):

    CHOICES = (
        ('price', 'Price Asc'),
        ('-price', 'Price Asc'),
        ('name', 'Name A-Z'),
        ('-name', 'Name Z-A'),
    )

    # sort = django_filters.ChoiceFilter(
    #     label='Sort by',
    #     choices=(
    #         ('price', 'Price'),
    #         ('name', 'Name')
    #     ),
    #     method='sort_name'
    # )
    #
    # def sort_name(self, queryset, name, value):
    #     if value == 'price':
    #         sort.field_name = 'price'
    #     elif value == 'name':
    #         sort.name = 'name'

    ordering = django_filters.ChoiceFilter(
        label='Ordering',
        choices=CHOICES,
        method='filter_by_order'
    )

    def filter_by_order(self, queryset, name, value):
        expression = value
        # expression = 'price' if value == 'price' else '-price'
        return queryset.order_by(expression)

    class Meta:
        model = Product
        fields = [
            # 'owner',
            # 'type',
            # 'name',
            # 'price',
            # 'description',
            # 'likes',
            # 'size',
            # 'address',
            # 'status',
            # 'flags',
        ]




