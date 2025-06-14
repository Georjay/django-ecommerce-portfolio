from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # e.g., 99999999.99
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set when product is created
    updated_at = models.DateTimeField(auto_now=True)     # Automatically set when product is updated

    def __str__(self):
        return self.name
