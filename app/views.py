from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, JsonResponse
from .models import Product

def hello_world(request):
    return HttpResponse("Hello World 2!")

def home(request):
    return HttpResponse("Welcome to the Homepage!")


def product_list(request):
    try:
        # Retrieve data using Django ORM
        products = Product.objects.all()
        print(products)  # Print the queryset for debugging
        
        # Convert queryset to a list of dictionaries
        product_list = list(products.values())
        print(product_list)  # Print the actual data retrieved
        
        # Pass the list of dictionaries to the template
        return render(request, 'product_list.html', {'products': product_list})
    except Exception as e:
        print(f"Error retrieving products: {e}")
        return JsonResponse({'error': str(e)}, status=500)


# def product_list(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM products")
#         products = cursor.fetchall()
#         print(products)  # This will print the raw data retrieved
#     return render(request, 'product_list.html', {'products': products})