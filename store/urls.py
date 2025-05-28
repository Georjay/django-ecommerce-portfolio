from django.urls import path
from . import views  # Import views from the current app

app_name = 'store' # This is optional but good practice for namespacing URLs

urlpatterns = [
    # When someone visits the 'root' of this app (e.g., /store/),
    # call the product_list view.
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:product_id>/', views.update_cart_item, name='update_cart_item'),
]