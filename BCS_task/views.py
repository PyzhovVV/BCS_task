from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from BCS_task.forms import UserForm
from BCS_task.models import Translation


def index(request):
    list_of_translation = Translation.objects.all()
    context = {
        'title': 'Главная страница',
        'list_of_translation': list_of_translation
    }
    return render(request, 'BCS_task/index.html', context=context)


def show_description(request, transaction_id):
    transaction = Translation.objects.get(id=transaction_id)
    return HttpResponse(f"""Отображение описания транзакции с id = {transaction_id}:
                        {transaction.description}""")


def about(request):
    context = {
        'title': 'О сайте',
        'my_git': 'https://github.com/PyzhovVV'
    }
    return render(request, 'BCS_task/about.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
