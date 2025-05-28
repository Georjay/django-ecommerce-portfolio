from django.urls import path
from . import views  # Import views from the current app

app_name = 'store' # This is optional but good practice for namespacing URLs

urlpatterns = [
    # When someone visits the 'root' of this app (e.g., /store/),
    # call the product_list view.
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail')
]