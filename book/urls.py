from . import signals

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.views import CategoryViewSet, BookViewSet, ReviewViewSet, AuthorViewSet, OrderViewSet

from book.services import UserBookViewCreate
from book.services import FlashSaleListCreateView, check_flash_sale
from book.services import admin_replenish_stock

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('sale/', FlashSaleListCreateView.as_view(), name='sale'),
    path('check-sale/<int:book_id>/', check_flash_sale, name='check-flash-sale'),
    path('book-view/', UserBookViewCreate.as_view(), name='user-book-view-create'),
    path('admin/replenish_stock/<int:book_id>/<int:amount>', admin_replenish_stock, name='admin_replenish_stock')
]
