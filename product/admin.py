from django.contrib import admin

# Register your models here.

from product.models import ProductModel

admin.site.register(ProductModel)