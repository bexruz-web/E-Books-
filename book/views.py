from django.db import models
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Author, Category, Book, Review
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer, ReviewSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        category = request.query_params.get('category', None)
        if category:
            self.queryset = self.queryset.filter(category=category)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        related_books = Book.objects.filter(category=instance.category).exclude(id=instance.id)[:5]
        related_serializer = BookSerializer(related_books, many=True)
        print(serializer.data)
        print(related_serializer.data)
        return Response({
            'book': serializer.data,
            'related_books': related_serializer.data
        })

    @action(detail=False, methods=['get'])
    def top_rating(self, request):
        top_books = Book.objects.annotate(avg_rating=models.Avg('reviews__rating')).order_by('-avg_rating')[:2]
        serializer = BookSerializer(top_books, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def average_rating(self, request, pk=None):
        book = self.get_object()
        reviews = book.reviews.all()

        if reviews.count() == 0:
            return Response({
                'average_rating': "No reviews yet!"
            })
        avg_rating = sum([review.rating for review in reviews]) / reviews.count()

        return Response({
            'average_rating': avg_rating
        })
