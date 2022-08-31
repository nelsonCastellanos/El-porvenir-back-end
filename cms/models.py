from django.db import models

from wagtail.models import Page
from colorfield.fields import ColorField
from wagtail.admin.panels import FieldPanel


# Create your models here.

class HomePage(Page):
    title_featured_categories = models.CharField(max_length=250)
    content_panels = Page.content_panels + [
        FieldPanel('title_featured_categories')
    ]

class HomeFeaturedCategory(Page):
    width =  models.IntegerField()
    color_texto = ColorField(default='#FF0000')
    description = models.TextField()
    content_panels = Page.content_panels + [
        FieldPanel('width'),
        FieldPanel('color_texto'),
        FieldPanel('description')
    ]