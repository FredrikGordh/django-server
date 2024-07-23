from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World 2!")

def home(request):
    return HttpResponse("Welcome to the Homepage!")