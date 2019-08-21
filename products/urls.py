from django.urls import path
from .views import (
    dynamic_lookup_view,
    product_list_view,
)


#This is used in products/model.py in the get_absolute_url function
app_name = "products"

urlpatterns = [
    path("<int:product_id>/", dynamic_lookup_view, name="product-detail"),
    path("", product_list_view, name="product-list"),
]