from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Order, OrderList


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