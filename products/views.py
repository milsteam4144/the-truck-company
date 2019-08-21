from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.db.models import Q

# These are function based views

'''
If there is a products directory with the file product_detail.html in both the "products" app
folder and in the templates folder, the one in the templates folder overrides the one in the 
"products" app folder. You can override any template that is in an app folder by placing a 
new html template with the same name in the templates folder. This is because django is looking
in the settings for the "DIR" filepath, which resolves to the "src's" templates folder.
'''
#Allows user to enter a number in the URL to view the product_detail.html page of that object
def dynamic_lookup_view(request, product_id):
    obj = get_object_or_404(Product, id= product_id)
    context = {
        "object":obj
    }
    return render(request, "products/product_detail.html", context)

    

#List all the objects in the Products table in product_list.html
#After an object is deleted, redirect here. TO DO - After a product is created, redirect here
def product_list_view(request):
    queryset = Product.objects.all() #Returns list of objects
    search_term = ""
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(
            Q(name__icontains=search_term) |
            Q(product_no=search_term))
    
    context = {
        "title":"All Products",
        "product_list": queryset,
        "search_term" : search_term,
    }
    return render(request, "products/product_list.html", context)