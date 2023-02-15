from django.shortcuts import render
from random import randint
from django.http import HttpResponse

from exercises_app.models import Article


def random_number(request):
    return HttpResponse(
        f"Wylosowano liczbę: {randint(0, 100)}"
    )


def random_number_max_min(request, min_number, max_number):
    return HttpResponse(
        f"Użytkownik podał wartość {min_number} i {max_number}. Wylosowano liczbę: {randint(min_number, max_number)}"
    )


def articles(request):
    return render(
        request,
        'exercises_app/articles.html',
        {
            'articles': Article.objects.filter(status=3)
        }
    )