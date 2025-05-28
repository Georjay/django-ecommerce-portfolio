from django.shortcuts import render, get_object_or_404
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

def product_detail(request, product_id):
    # Get a single product by its id (primary key)
    # If the product with that id doesn't exist, it will show a 404 page
    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product
    }
    return render(request, 'store/product_detail.html', context)
