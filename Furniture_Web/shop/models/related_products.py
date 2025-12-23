from django.db import models
from .product import Product

class RelatedProduct(models.Model):
    product = models.ForeignKey(Product, related_name='related_products', on_delete=models.CASCADE)
    related_product = models.ForeignKey(Product, related_name='related_to', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title} related to {self.related_product.title}"
