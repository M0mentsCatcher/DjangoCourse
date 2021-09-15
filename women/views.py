import datetime

from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
from django.shortcuts import redirect


def index(requset):  # HttpRequest
    return HttpResponse('Страница приложения women')


def categories(req, catid):
    if req.GET:
        print(req.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')


def archive(req, year):
    if int(year) > datetime.date.today().year:
        return redirect('home', permanent=False)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(req, exception):
    return HttpResponseNotFound('<h1>Страничка не найдена(((</h1>')
