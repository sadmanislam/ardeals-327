from __future__ import unicode_literals
#from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from django.urls import reverse


#class User(models.Model):
 #   firstName = models.CharField(max_length=550)
  #  lastName = models.CharField(max_length=550)
   # email = models.CharField(max_length=550)
    #password = models.CharField(max_length=550)
    #type = models.CharField(max_length=550)

    #def __str__(self):
     #   return self.firstName + ' ' + self.lastName


class Area(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Deal(models.Model):
    publisher = models.CharField(max_length=250)
    description_small = models.TextField()
    description_long = models.TextField()
    # user_rating = IntegerField(default=0, max_length=5)
    # user_rating = models.PositiveSmallIntegerField(default=0)
    # ratings = GenericRelation(Rating, related_query_name='rating')
    # ratings = models.int()
    main_attraction = models.CharField(max_length=250)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    genre = models.CharField(max_length=250)
    contact = models.CharField(max_length=15)
    validity = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=550)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    city = models.CharField(max_length=550, default="Dhaka")
    country = models.CharField(max_length=550, default="Bangladesh")
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
    thumbnail = models.FileField()

    def get_absolute_url(self):
        return reverse('deal:alldeals')

    def __str__(self):
        return self.publisher + ' - ' + self.description_small + ' - ' + str(self.validity)

    def sites_str(self):
        return ', '.join([s.name for s in self.sites.all()])

    sites_str.short_description = 'sites'

    #Deal.objects.filter(ratings__isnull=False).order_by('ratings__average')


@python_2_unicode_compatible
class Vote(models.Model):
    """A Vote on a Deal"""
    user = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)
    product = models.ForeignKey(Deal, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return "Vote"




