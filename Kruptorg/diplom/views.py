from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import OrderList, Order
from .serializers import OrderSerializer


def index(request):
    return HttpResponse("Главная страница")

def index2(request, category):
    return HttpResponse(f'Категория {category}')

def order_create(request):
    if request.method == 'GET':
        order = Order.objects.get()
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data)

