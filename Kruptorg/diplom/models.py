from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=30)
    date = models.DateTimeField()
    status = models.CharField(max_length=30)
    car_number = models.CharField(max_length=30)
    pricep_number = models.CharField(max_length=30)
    places = models.IntegerField()
    names = models.IntegerField()


class Sostav_zakaza (models.Model):
    name = models.CharField(max_length=200)
    mass = models.FloatField()
    count = models.IntegerField()
    ed_izm = models.CharField(max_length=20)
    place = models.IntegerField()
    sht_place = models.IntegerField()
