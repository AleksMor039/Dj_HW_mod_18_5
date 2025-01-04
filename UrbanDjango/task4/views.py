from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Platform(TemplateView):
    template_name = 'platform.html'


class Cart(TemplateView):
    template_name = 'cart.html'


def menu(request):
    mydict_games = {'games': ['Need for speed', 'Atomic Heart', 'Far Cry']}
    context = {
        'mydict_games': mydict_games,
    }
    return render(request, 'games.html', context)
