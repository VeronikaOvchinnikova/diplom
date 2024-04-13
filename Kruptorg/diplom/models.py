from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=30) #NOT null?
    date = models.DateTimeField()
    status = models.CharField(max_length=30) #по дефолту "Принят"
    car_number = models.CharField(max_length=30)
    trailer_number = models.CharField(max_length=30) #номер прицепа
    places = models.IntegerField()
    names = models.IntegerField()


class OrderList(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mass = models.DecimalField(max_digits=20, decimal_places=3)
    count = models.IntegerField()
    unit = models.CharField(max_length=20) #единица измерения
    place = models.IntegerField()
    unit_place = models.IntegerField() #штука-место
