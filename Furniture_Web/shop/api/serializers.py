from rest_framework import serializers
from shop.models.product import Product
from shop.models.variant import Variant
from shop.models.vendor import Vendor
from shop.models.category import Category
from shop.models.buy_together import BuyTogether
from shop.models.related_products import RelatedProduct



class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['id', 'title', 'price', 'variant_id']


class ProductSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()
    general_category = CategorySerializer()
    variants = VariantSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'  


class BuyTogetherSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    recommended_product = ProductSerializer()

    class Meta:
        model = BuyTogether
        fields = ['id', 'product', 'recommended_product']


class RelatedProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    related_product = ProductSerializer()

    class Meta:
        model = RelatedProduct
        fields = ['id', 'product', 'related_product']
