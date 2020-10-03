from django.contrib import admin
from .models import Product

# Register your models here.

class ProductDisplay(admin.ModelAdmin):
    fieldsets = [
        ("Title/Date", {"fields": ["product_title", "product_added"]}),
        ("Content", {"fields": ["product_content", "product_thumbnail",
                                "product_url",
                                "product_price"]
                     })
        ]

admin.site.register(Product, ProductDisplay)
