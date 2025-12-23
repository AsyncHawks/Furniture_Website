from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet, VariantViewSet, BuyTogetherViewSet, RelatedProductViewSet
from .views import products_by_category, products_by_vendor


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'variants', VariantViewSet)
router.register(r'buy-together', BuyTogetherViewSet)
router.register(r'related-products', RelatedProductViewSet)







urlpatterns = [
    path('api/', include(router.urls)),
    path('api/products/category/<int:category_id>/', products_by_category, name='products_by_category'),
    path('api/products/vendor/<int:vendor_id>/', products_by_vendor, name='products_by_vendor'),
]
