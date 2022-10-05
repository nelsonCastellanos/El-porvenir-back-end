from unicodedata import category
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField

class Product(models.Model):
    code_siigo = models.IntegerField()
    name = models.CharField(max_length=100)
    iva = models.IntegerField()
    description = models.CharField(max_length=500)
    cantidad = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=9)
    images =  StreamField([
        ('image', ImageChooserBlock()),
    ])

    panels = [
        FieldPanel('code_siigo'),
        FieldPanel('name'),
        FieldPanel('images')
    ]


    def __str__(self):
        return self.name