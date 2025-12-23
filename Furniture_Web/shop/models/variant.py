from django.db import models
from .product import Product

class Variant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    # variant_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.title} - {self.product.title}"
