from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    product_thumbnail = models.ImageField(blank=True, upload_to='products_images/', max_length=500)
    product_title = models.CharField(max_length=200)
    product_content = models.TextField()
    product_price = models.IntegerField(default=0)
    product_url = models.URLField(blank=True, max_length=250)
    product_added = models.DateTimeField("date added", default=datetime.now())

    def __str__(self):
        return self.product_title


