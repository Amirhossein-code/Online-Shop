from .customer_serializers import (
    SimpleCustomerSerializer,
    UpdateCustomerSerializer,
    DetailedCustomerSerializer,
)
from .category_serializers import CategorySerializer
from .product_serializers import (
    ProductSerializer,
    SimpleProductSerializer,
    ProductImageSerializer,
)
from .cart_serializers import (
    CartItemSerializer,
    AddCartItemSerializer,
    UpdateCartItemSerializer,
    CartSerializer,
)
from .order_serailziers import (
    OrderSerializer,
    OrderItemSerializer,
    UpdateOrderSerializer,
    CreateOrderSerializer,
)
