from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Главная страница")

def index2(request, category):
    return HttpResponse(f"Категория {category}")

