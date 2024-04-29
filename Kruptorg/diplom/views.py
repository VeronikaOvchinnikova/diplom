from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import OrderList, Order
from .serializers import OrderSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated


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




