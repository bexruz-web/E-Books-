from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    full_name = models.CharField(max_length=200)
    birth_year = models.CharField(max_length=15, blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    file = models.FileField(upload_to='books/')
    publication_date = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.PositiveIntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.rating}"


