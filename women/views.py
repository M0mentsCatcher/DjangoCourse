from django.http import HttpResponse


# Create your views here.
def index(requset):  # HttpRequest
    return HttpResponse('Страница приложения women')


def categories(req):
    return HttpResponse('<h1>Статьи по категориям</h1>')
