from django.shortcuts import render

# Create your views here.
def index(requset): # HttpRequest
    return HttpResponse('Страница приложения women')