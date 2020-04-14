from django.contrib import admin
from .models import Favorite, Category, Product, Store

# Register your models here.
admin.site.register(Favorite)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Store)
