from rest_framework.routers import DefaultRouter
from api.products.views import ProductViewset

router = DefaultRouter()
router.register('', ProductViewset, basename='product')
urlpatterns = router.urls
