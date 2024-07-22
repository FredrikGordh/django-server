from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!")

def home(request):
    return HttpResponse("Welcome to the Homepage!")