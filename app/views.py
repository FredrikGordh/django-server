from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .models import YourModel

def hello_world(request):
    return HttpResponse("Hello World 2!")

def home(request):
    return HttpResponse("Welcome to the Homepage!")

# def data_view(request):
#     data = list(YourModel.objects.values())
#     return JsonResponse(data, safe=False)