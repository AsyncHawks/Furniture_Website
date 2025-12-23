from rest_framework import viewsets
from .serializers import (
    ProductSerializer,
    VariantSerializer,
    BuyTogetherSerializer,
    RelatedProductSerializer,
)

from shop.models.product import Product
from shop.models.variant import Variant
from shop.models.buy_together import BuyTogether
from shop.models.related_products import RelatedProduct


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class VariantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer


class BuyTogetherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BuyTogether.objects.all()
    serializer_class = BuyTogetherSerializer


class RelatedProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RelatedProduct.objects.all()
    serializer_class = RelatedProductSerializer





