from accounts.api.viewsets import OrderItemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
# router.register( r'Order',OrderViewSet)
router.register( r'OrderItem',OrderItemViewSet)

urlpatterns = router.urls