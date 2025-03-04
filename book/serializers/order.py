from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from book.models import Book, Order


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'book', 'customer', 'quantity', 'created_at', 'total_price', 'phone_number', 'is_paid']

    def get_total_price(self, obj):
        return obj.book.price * obj.quantity

    def validate_quantity(self, value):
        try:
            book_id = self.initial_data['book']
            book = Book.objects.get(id=book_id)

            # Check the stock
            if value > book.stock:
                raise serializers.ValidationError("Not enough items in stock.")

            if value < 1:
                raise serializers.ValidationError("Quantity must be at least 1")

            return value
        except ObjectDoesNotExist:
            raise serializers.ValidationError("Book does not exist")

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        book = order.book
        book.stock -= order.quantity
        book.save()
        return order

