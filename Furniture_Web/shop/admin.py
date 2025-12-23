from django.contrib import admin
from .models.product import Product
from .models.variant import Variant
from .models.vendor import Vendor
from .models.category import Category
from .models.buy_together import BuyTogether
from .models.related_products import RelatedProduct
from .models.collections import Collection
from .models.product_image import ProductImage  

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'available_in', 'items_in_stock')  
    search_fields = ('title', 'description')
    filter_horizontal = ('collections',)  
    inlines = [ProductImageInline]

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'image') 
    search_fields = ('title',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Variant)
admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(BuyTogether)
admin.site.register(RelatedProduct)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(ProductImage)
