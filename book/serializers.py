from rest_framework import serializers
from .models import Book, Review, Category, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True, required=False)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'description', 'price', 'file', 'publication_date', 'avg_rating']
