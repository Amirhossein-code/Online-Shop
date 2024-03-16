from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register("customer", views.CustomerViewSet, basename="customer")


urlpatterns = router.urls
