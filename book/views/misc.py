from book.models import Author, Category, Review, Order
from book.serializers import AuthorSerializer, CategorySerializer, ReviewSerializer, OrderSerializer

from book.permissions import IsOwnerOrReadOnly

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    permission_classes = [IsOwnerOrReadOnly]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ['full_name']

    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAuthenticated]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
