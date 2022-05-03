from django.contrib import admin
from product.models import Product,ProductCategory

admin.site.register([Product,ProductCategory])
