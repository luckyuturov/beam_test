from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, VendorViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'vendors', VendorViewSet)

urlpatterns = router.urls
