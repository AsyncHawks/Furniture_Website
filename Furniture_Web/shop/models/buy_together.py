from django.db import models
from .product import Product

class BuyTogether(models.Model):
    product = models.ForeignKey(Product, related_name='buy_together', on_delete=models.CASCADE)
    recommended_product = models.ForeignKey(Product, related_name='recommended_by', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title} with {self.recommended_product.title}"
