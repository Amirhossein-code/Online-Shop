from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register("customer", views.CustomerViewSet, basename="customer")
router.register("categories", views.CategoryViewSet, basename="categories")
router.register("products", views.ProductViewSet, basename="products")


urlpatterns = router.urls
