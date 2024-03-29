# from django.dispatch import receiver
# from ..signals import order_created
# from ..models import Ship


# @receiver(order_created)
# def create_ship_for_order(sender, **kwargs):
#     order = kwargs.get("order")
#     customer = order.customer
#     address = customer.address.filter(main=True).first()

#     ship = Ship.objects.create(order=order, customer=customer, address=address)

#     # Add order items to the ship
#     for item in order.items.all():
#         ship.order_items.add(item)

#     # Calculate and store the total price in the ship object
#     ship.total_price = ship.total_price()
#     ship.save()
