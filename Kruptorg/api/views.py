from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets, status
from djoser.views import TokenCreateView

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from diplom.models import Order, OrderList
from .serializers import OrderSerializer, OrderListSerializer


class AddOrderView(viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
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
    serializer_class = OrderListSerializer
    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def add_order_list(self, request):
        order_number = request.data.get('order_number')
        if not order_number:
            return Response({
                'status': 'Error occured',
                'errors': 'order_number is required'
            },
                status=status.HTTP_400_BAD_REQUEST)
        order = get_object_or_404(Order, order_number=order_number)
        items = request.data.get('items')
        if not items:
            return Response({
                'status': 'Error occured',
                'errors': 'items is required'
            },
                status=status.HTTP_400_BAD_REQUEST)
        for item in items:
            item_name = item.get('name')
            item_object = OrderList.objects.filter(order=order, name=item_name).first()
            if item_object:
                for key, value in item.items():
                    setattr(item_object, key, value)
                item_object.save()
            else:
                item['order'] = order.id
                serializer = OrderListSerializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response({
                        'status': 'Error occured',
                        'errors': serializer.errors
                    },
                        status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'status': f'Items added to order {order.order_number}'
        },
                        status=status.HTTP_201_CREATED)


# class TokenCreationView(TokenCreateView):
#     pass