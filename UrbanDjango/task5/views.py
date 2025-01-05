'''
Напишите 2 представления sign_up_by_django и sign_up_by_html.
'''

from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

# псевдо-список
users = [
    'aleks', 'vlad', 'nikita',
    'olga', 'sveta', 'lena'
]


# Create your views here.
def sign_up_by_html(request):
    info = {}  # пустой словарь
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if username in users:
            info['error'] = f"Пользователь {username} уже существует"

        elif len(password) < 8:
            info['error'] = f"Пароль должен быть не менее 8 символов"

        elif repeat_password != password:
            info['error'] = f"Пароли не совпадают"

        elif int(age) < 18:
            info['error'] = f"Вы должны быть старше 18"

        else:
            info['text'] = f"Приветсвуем, {username}!"

    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    info = {}  # пустой словарь

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = f"Пользователь {username} уже существует"
                return HttpResponse(f'Пользователь {username} уже существует')

            elif len(password) < 8:
                info['error'] = "Пароль должен быть не менее 8 символов"
                return HttpResponse(f'Пароль должен быть не менее 8 символов')

            elif repeat_password != password:
                info['error'] = "Пароли не совпадают"
                return HttpResponse(f'Пароли не совпадают')

            elif int(age) < 18:
                info['error'] = f"Вы должны быть старше 18"
                return HttpResponse(f'Вы должны быть старше 18')

            else:
                info['text'] = f"Приветствуем, {username}!"
            return HttpResponse(f'Приветствуем, {username}!')

    else:
        form = UserRegister()
        info['message'] = form
    return render(request, 'registration_page.html', info)
