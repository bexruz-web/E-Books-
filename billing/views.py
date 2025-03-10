from rest_framework import views, status
from rest_framework.response import Response

import stripe

from config.settings import STRIPE_SECRET_KEY

from .models import Payment
from book.models import Order
from .serializers import PaymentSerializer

stripe.api_key = STRIPE_SECRET_KEY


class CreateChargeView(views.APIView):

    def post(self, request, *args, **kwargs):
        stripe_token = request.data.get('stripe_token')
        order_id = request.data.get('order_id')

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': "Order not found"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            total_amount = order.book.price * order.quantity
            charge = stripe.Charge.create(
                amount=int(total_amount*100),
                currency='uzs',
                source=stripe_token,
            )

            Payment.objects.create(
                order=order,
                stripe_charge_id=charge['id'],
                amount=total_amount
            )

            order.is_paid = True
            order.save()

            return Response({"status": "Payment successful"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
