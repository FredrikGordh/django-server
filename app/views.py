from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product

def hello_world(request):
    return HttpResponse("Hello World 2!")

def home(request):
    return HttpResponse("Welcome to the Homepage!")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})