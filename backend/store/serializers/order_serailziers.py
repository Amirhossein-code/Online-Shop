from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from django.db import transaction
from ..models import Order, OrderItem, Cart, CartItem, Customer, Address
from ..serializers import SimpleProductSerializer
from ..signals import order_created
from ..signals import order_created


class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "quantity",
            "unit_price",
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "placed_at",
            "payment_status",
            "customer",
            "items",
        ]


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["payment_status"]


class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError("No cart with the given ID was found.")
        if CartItem.objects.filter(cart_id=cart_id).count() == 0:
            raise serializers.ValidationError("The cart is empty.")
        return cart_id

    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data["cart_id"]
            customer = Customer.objects.get(user_id=self.context["user_id"])

            try:
                address = Address.objects.get(customer=customer, main=True)
            except ObjectDoesNotExist:
                raise serializers.ValidationError(
                    "No main address found for the customer."
                )

            # Create Order obj
            order = Order.objects.create(customer=customer)

            # get the cart in db by the cart ID posted
            cart_items = CartItem.objects.select_related("product").filter(
                cart_id=cart_id
            )

            # Create Order items for the created Order obj
            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    unit_price=item.product.unit_price,
                    quantity=item.quantity,
                )
                for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)

            # Delete the cart instance since Order is created with associated OrderItems
            Cart.objects.filter(pk=cart_id).delete()

            # TODO : Rediret User to The payment gateway
            # TODO : Send a signal to shipping model to generate a ship obj
            order_created.send_robust(self.__class__, order=order, address=address)

            return order
