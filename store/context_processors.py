from .models import Product # Though not strictly needed here if only using cart session data for count/total
from decimal import Decimal

def cart_summary(request):
    cart = request.session.get('cart', {}) #Gets the cart dictionary from the session
    cart_item_count = 0
    cart_total_price = Decimal('0.00')

    for product_id_str, item_data in cart.items():
        cart_item_count += item_data.get('quantity', 0) # Use .get() for safety
        price = item_data.get('price', '0.00')
        quantity = item_data.get('quantity', 0)
        cart_total_price += Decimal(price) * quantity

    return {
        'cart_item_count': cart_item_count,
        'cart_total_price': cart_total_price,
    }