from django.contrib import admin
from .models import Product

admin.site.register(Product) # Tell the admin to manage Product
