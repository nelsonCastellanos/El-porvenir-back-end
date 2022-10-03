from unicodedata import category
from django.db import models

from category.models import Category


class Product(models.Model):
    code_siigo = models.IntegerField()
    name = models.CharField(max_length=100)
    iva = models.IntegerField()
    description = models.CharField(max_length=500)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_length=100)
    category = models.ManyToManyField(Category)
