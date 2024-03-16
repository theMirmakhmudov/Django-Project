from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=224)
    address = models.CharField(max_length=224)
    age = models.IntegerField()
