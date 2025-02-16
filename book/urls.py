from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, BookViewSet, ReviewViewSet, AuthorViewSet

from .services.book_view_history import UserBookViewCreate
from .services.flash_sale import FlashSaleListCreateView, check_flash_sale
router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('sale/', FlashSaleListCreateView.as_view(), name='sale'),
    path('check-sale/<int:book_id>/', check_flash_sale, name='check-flash-sale'),
    path('book-view/', UserBookViewCreate.as_view(), name='user-book-view-create'),

]