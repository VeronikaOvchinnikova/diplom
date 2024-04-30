from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from diplom.models import Order, OrderList


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_number',
                  'date',
                  'status',
                  'car_number',
                  'trailer_number',
                  'places',
                  'names')

    def validate_order(self, order_number):
        order = get_object_or_404(Order, order_number=order_number).first()
        if order:
            raise serializers.ValidationError('Не может быть двух заказов с одним номером')
        return order




class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderList
        fields = ('order',
                  'name',
                  'mass',
                  'count',
                  'unit',
                  'place',
                  'unit_place')

    # def validate_order(self, name):
    #     names = get_objects_or_404(OrderList, name=name)
    #     if len(names) > 1:
    #         raise serializers.ValidationError(
    #             'Не может быть двух составов заказа с одним номером')
    #     name = get_object_or_404(OrderList, name=name).first()
    #     return name
