from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Order, OrderList
from api.serializers import OrderSerializer


class IndexListView(ListView):
    paginate_by = 10
    model = Order
    template_name = 'index.html'

    @action(
        methods=['POST', 'PATCH'],
        detail=False,
        permission_classes=(IsAuthenticated, ),
        url_path='add_order',
        url_name='add_order'
    )
    def add_order(self, request):
        pass




