from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def platform(request):
    title = 'Игровая платформа'
    text1 = 'Главная страница'
    text2 = 'Главная'
    text3 = 'Магазин'
    text4 = 'Корзина'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': text3,
        'text4': text4
    }
    return render(request, 'platform.html', context)


def games(request):
    title = 'Магазин'
    text = 'Игры'
    game1 = 'Need for speed'
    game2 = 'Atomic Heart'
    game3 = 'Far Cry'
    context = {
        'title': title,
        'text': text,
        'g1': game1,
        'g2': game2,
        'g3': game3
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    text1 = 'Моя корзина'
    text2 = 'Корзина пуста! - Может пополним и поиграем?'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2
    }
    return render(request, 'cart.html', context)
