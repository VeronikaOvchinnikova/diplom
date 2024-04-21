from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import OrderList, Order
from .serializers import OrderSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView


def index(request):
    return HttpResponse("Главная страница")

def index2(request, category):
    return HttpResponse(f'Категория {category}')

def order_create(request):
    if request.method == 'GET':
        order = Order.objects.get()
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data)

class IndexListView(ListView):
    paginate_by = 10
    model = Order
    template_name = 'index.html'

