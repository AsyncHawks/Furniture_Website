from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()  # URL field to store the link
    image = models.ImageField(upload_to='collections_images/')  # ImageField to store collection images

    def __str__(self):
        return self.title
