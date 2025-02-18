from django_filters import rest_framework as django_filters # pip install django-filter
from .models import Book, FlashSale


class BookFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['category', 'min_price', 'max_price']


class FlashSaleFilter(django_filters.FilterSet):
    class Meta:
        model = FlashSale
        fields = ['book', 'discount_percentage']
