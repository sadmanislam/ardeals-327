from django.db import models
from datetime import datetime


class User(models.Model):
    firstName = models.CharField(max_length=550)
    lastName = models.CharField(max_length=550)
    email = models.CharField(max_length=550)
    password = models.CharField(max_length=550)
    type = models.CharField(max_length=550)

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Area(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Deal(models.Model):
    publisher = models.CharField(max_length=250)
    description_small = models.TextField()
    description_long = models.TextField()
    user_rating = models.PositiveSmallIntegerField()
    keyword1 = models.CharField(max_length=250)
    keyword2 = models.CharField(max_length=250)
    keyword3 = models.CharField(max_length=250)
    contact = models.CharField(max_length=15)
    validity = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    street = models.CharField(max_length=550)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    city = models.CharField(max_length=550)
    country = models.CharField(max_length=550)
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deal_logo = models.CharField(max_length=1000, default='xxx')

    objects = models.Manager()
    #thumbnail
    #image

    def __str__(self):
        return self.description_small + ' - ' + self.publisher + ' - ' + str(self.validity)

