from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Order, OrderList
from django.shortcuts import get_object_or_404


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