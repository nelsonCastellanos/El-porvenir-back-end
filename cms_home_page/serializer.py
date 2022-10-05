from rest_framework import serializers
from wagtail.admin.api.serializers import PageAncestorsField, AdminPageSerializer
from wagtail.api.v2.serializers import get_serializer_class
from wagtail.images.api.fields import ImageRenditionField
from wagtail.models import Page


class HomePageSectionBlockSerializer(serializers.Serializer):
    largo = serializers.IntegerField()
    titulo = serializers.CharField()
    descripcion = serializers.CharField()
    color = serializers.CharField()
    imagen = serializers.SerializerMethodField()
    page = serializers.SerializerMethodField()

    def get_imagen(self, blocks):
        if blocks['imagen'] is not None:
            imagen = ImageRenditionField(
                'height-' + str(blocks['largo'])).to_representation(
                    blocks['imagen'])
            return imagen
        return None

    def get_page(self, obj):
        if obj['page'] is not None:
            serializer_class = get_serializer_class(
                Page,
                ['id', 'title'],
                meta_fields=[],
                base=AdminPageSerializer,
            )
            page = serializer_class().to_representation(obj['page'])
            return page
        return None


class HomePageSlideBlockSerializer(serializers.Serializer):
    imagen = serializers.SerializerMethodField()
    pagina = serializers.SerializerMethodField()

    def get_imagen(self, blocks):
        if blocks['imagen'] is not None:
            imagen = ImageRenditionField('fill-2000x600').to_representation(
                blocks['imagen'])
            return imagen
        return None

    def get_pagina(self, obj):
        if obj['pagina'] is not None:
            serializer_class = get_serializer_class(
                Page,
                ['id', 'title'],
                meta_fields=[],
                base=AdminPageSerializer,
            )
            page = serializer_class().to_representation(obj['page'])
            return page
        return None
