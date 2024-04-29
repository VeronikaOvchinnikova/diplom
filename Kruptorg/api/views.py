from django.shortcuts import render
from rest_framework import viewsets, status

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from diplom.models import Order, OrderList
from .serializers import OrderSerializer, OrderListSerializer


class AddOrderView(viewsets.GenericViewSet):
    @action(detail=False, methods=['POST'], permission_classes=[AllowAny], url_path='add_order', url_name='add_order')
    def add_order(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': f'Order created for {request.data["order_number"]}'
            },
                status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Error occured',
            'errors': serializer.errors
        },
            status=status.HTTP_400_BAD_REQUEST)




class AddOrderListView(viewsets.GenericViewSet):
    def add_order_list(self, request):
        serializer = OrderListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': f'OrderList created for {request.data.order}'
            },
                status=status.HTTP_201_CREATED)
        return Response({'status': f'Error occured for {request.data.order}'
            },
                status=status.HTTP_400_BAD_REQUEST)

