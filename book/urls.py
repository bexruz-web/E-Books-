from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, BookViewSet, ReviewViewSet, AuthorViewSet

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls))
]