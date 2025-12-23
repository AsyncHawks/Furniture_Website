from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.models.product import Product
from shop.models.collections import Collection
from .serializers import ProductSerializer

@api_view(['GET'])
def products_by_category(request, category_id):
    products = Product.objects.filter(general_category__id=category_id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def products_by_vendor(request, vendor_id):
    products = Product.objects.filter(vendor__id=vendor_id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def products_in_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    products = collection.products.all()  # Get all products in this collection
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)