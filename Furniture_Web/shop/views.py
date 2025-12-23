# from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Product, Variant, BuyTogether, RelatedProduct
# from .api.serializers import ProductSerializer, VariantSerializer, BuyTogetherSerializer, RelatedProductSerializer


# class ProductViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class VariantViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Variant.objects.all()
#     serializer_class = VariantSerializer


# class BuyTogetherViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = BuyTogether.objects.all()
#     serializer_class = BuyTogetherSerializer


# class RelatedProductViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = RelatedProduct.objects.all()
#     serializer_class = RelatedProductSerializer


# @api_view(['GET'])
# def products_by_category(request, category_id):
#     products = Product.objects.filter(general_category__id=category_id)
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def products_by_vendor(request, vendor_id):
#     products = Product.objects.filter(vendor__id=vendor_id)
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

