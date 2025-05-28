from django.shortcuts import render
from .models import Product

def product_list(request):
    # Get all Product objects from the database
    products = Product.objects.all()

    # Create a context dictionary to pass data to the template
    # The keys in this dictionary (e.g., 'products') will be
    # the variable names we use in the template.
    context = {
        'products': products
    }

    return render(request, 'store/product_list.html', context)
