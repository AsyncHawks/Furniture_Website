from django.db import models
from .vendor import Vendor
from .category import Category
from .collections import Collection

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.JSONField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    collections = models.ManyToManyField(Collection, related_name='products')
    features = models.JSONField()
    images = models.ImageField(upload_to='product_images/')
    free_shipping = models.BooleanField(default=False)
    available_in = models.CharField(max_length=50)
    sold = models.IntegerField(default=0)
    items_in_stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    general_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title
