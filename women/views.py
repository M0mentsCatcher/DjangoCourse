import datetime

from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
from django.shortcuts import redirect, render
from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):  # HttpRequest
    posts = Women.objects.all()
    return render(request, 'women/index.html',
                  {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О Сайте'})


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
