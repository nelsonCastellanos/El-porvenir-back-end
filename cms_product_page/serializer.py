from rest_framework import serializers
from wagtail.images.api.fields import ImageRenditionField


class ProductPageCategoryBlockSerializer(serializers.Serializer):
    titulo = serializers.CharField()
    imagen = serializers.SerializerMethodField()
    page = serializers.SerializerMethodField()

    def get_imagen(self, blocks):
        if blocks['imagen'] is not None:
            imagen = ImageRenditionField('height-' + str(blocks['largo'])).to_representation(blocks['imagen'])
            return imagen
        return None
