from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from decimal import Decimal #To accurately work with prices

def product_list(request):
    # Get all Product objects from the database
    products = Product.objects.all()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    # Create a context dictionary to pass data to the template
    # The keys in this dictionary (e.g., 'products') will be
    # the variable names we use in the template.
    context = {
        'products': products,
        'num_visits': num_visits,
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

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {}) # Get cart from session, or an empty dict if not present

    # For simplicity, we'll always add 1 quantity for now.
    # You could extend this to take quantity from a form.
    quantity_to_add = 1

    # Convert product_id to string because session keys are typically strings
    product_id_str = str(product.id)

    if product_id_str in cart:
        # If product is already in cart, increment quantity
        # Consider checking against product.stock here if needed
        cart[product_id_str]['quantity'] += quantity_to_add
    else:
        # If product is not in cart, add it
        # We store price in cart in case product price changes later
        cart[product_id_str] = {'quantity': quantity_to_add, 'price': str(product.price)}

    request.session['cart'] = cart # Save the updated cart back into the session
    # request.session.modified = True # Sometimes needed if you modify nested dicts, but usually assignment works

    messages.success(request, f"'{product.name}' has been added to your cart.") # Optional feedback
    return redirect('store:product_list') # Redirect to product list, or 'store:view_cart' or request.META.get('HTTP_REFERER', 'store:product_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_cart_price = Decimal('0.00') #Initialize as decimal

    # This loop processes items if the cart is NOT empty.
    # If 'cart' is empty, this loop will simply be skipped.
    for product_id_str, item_data in cart.items():
        try:
            product = Product.objects.get(id=int(product_id_str))
            total_item_price = Decimal(item_data['price']) * item_data['quantity']
            cart_items.append({
                'product': product,
                'quantity': item_data['quantity'],
                'price': Decimal(item_data['price']), # Store as Decimal
                'total_item_price': total_item_price,
            })
            total_cart_price += total_item_price
        except Product.DoesNotExist:
            # Handle case where a product in cart might have been deleted
            # For now, we can just skip it or remove it from cart
            # (More advanced: messages.error(request, f"Product with ID {product_id_str} not found and was removed from cart."))
            pass # Or implement removal logic

    context = {
        'cart_items': cart_items,
        'total_cart_price': total_cart_price,
        'is_empty': not bool(cart_items) # A flag to check if cart is empty
    }
    return render(request, 'store/cart_detail.html', context)

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id) # Ensure product_id is a string for dictionary key lookup

    if product_id_str in cart:
        # Get product name for the message before deleting
        # This part is optional for the message, but nice to have
        product_name = "The item" # Default name
        try:
            # Try to get the actual product name for a more informative message
            product = Product.objects.get(id=product_id)
            product_name = product.name
        except Product.DoesNotExist:
            pass # If product doesn't exist anymore, proceed with removal from cart using default name

        del cart[product_id_str]  # Remove the item from the cart dictionary
        request.session['cart'] = cart # Save the updated cart back to the session
        messages.success(request, f"'{product_name}' has been removed from your cart.")
    else:
        messages.warning(request, "Item not found in your cart.") # Or handle as you see fit

    return redirect('store:view_cart') # Redirect back to the cart page
