import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Order(models.Model):
    description_text = models.CharField(max_length=200)
    date = models.DateTimeField('date made')
    user = models.ForeignKey(User, null=True, blank=True, )

    def __str__(self):
        return self.description_text

    def was_recent(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

    was_recent.admin_order_field = 'date'
    was_recent.boolean = True
    was_recent.short_description = 'Recent?'


class Drink(models.Model):
    order = models.ForeignKey(Order,)
    type_of_drink = models.CharField(max_length=200)
    placed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.type_of_drink
