from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register("customers", views.CustomerViewSet, basename="customers")
router.register("addresses", views.AddressViewSet, basename="addresses")
router.register("categories", views.CategoryViewSet, basename="categories")
router.register("products", views.ProductViewSet, basename="products")
router.register("carts", views.CartViewSet, basename="carts")
router.register("orders", views.OrderViewSet, basename="orders")


products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("images", views.ProductImageViewSet, basename="product-images")
products_router.register(
    "reviews", views.ProductReviewViewSet, basename="product-reviews"
)
products_router.register(
    "my-reviews", views.MyProductReviewViewSet, basename="product-my-reviews"
)

carts_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
carts_router.register("items", views.CartItemViewSet, basename="cart-items")

urlpatterns = []

urlpatterns += router.urls + products_router.urls + carts_router.urls
