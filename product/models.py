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
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    cover_image = StreamField([('image', ImageChooserBlock())],
                              use_json_field=True,
                              max_num=1,
                              collapsed=False)
    images = StreamField([
        ('image', ImageChooserBlock(required=False)),
    ],
                         use_json_field=True)

    panels = [
        FieldPanel('code_siigo'),
        FieldPanel('name'),
        FieldPanel('iva'),
        FieldPanel('description'),
        FieldPanel('quantity'),
        FieldPanel('price'),
        FieldPanel('images'),
        FieldPanel('cover_image')
    ]

    def __str__(self):
        return self.name