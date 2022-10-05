from django import forms
from rest_framework import serializers
from wagtail.api import APIField
from wagtail.blocks import PageChooserBlock
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from cms_home_page.field_block import ColorFieldBlock
from cms_home_page.serializer import HomePageSectionBlockSerializer, HomePageSlideBlockSerializer




class HomePageSectionBlock(blocks.StructBlock):
    largo = blocks.IntegerBlock()
    titulo = blocks.CharBlock()
    descripcion = blocks.CharBlock()
    imagen = ImageChooserBlock()
    page = PageChooserBlock(label="page", required=False)
    color = ColorFieldBlock(default="#000000")

    class Meta:
        icon = 'user'
        form_classname = 'formset struct-block'

    def get_api_representation(self, value, context=None):
        serializer = HomePageSectionBlockSerializer(value)
        return serializer.data


class HomePageSlideBlock(blocks.StructBlock):
    imagen = ImageChooserBlock()
    pagina = PageChooserBlock(label="page", required=False)

    class Meta:
        icon = 'house'
        form_classname = 'formset struct-block'

    def get_api_representation(self, value, context=None):
        serializer = HomePageSlideBlockSerializer(value)
        return serializer.data


class HomePage(Page):
    slider = StreamField([
        ('slider', HomePageSlideBlock())
    ], use_json_field=True)
    secciones = StreamField([
        ('seccion', HomePageSectionBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('slider'),
        FieldPanel('secciones'),
    ]

    # export fields over the api
    api_fields = [
        APIField('slider'),
        APIField('secciones'),
    ]
