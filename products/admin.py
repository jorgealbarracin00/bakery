from django.contrib import admin
from .models import Ingredient, Supplier, Brand

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Supplier)
admin.site.register(Brand)
