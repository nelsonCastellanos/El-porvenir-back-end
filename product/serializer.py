from rest_framework import serializers
from wagtail.images.api.fields import ImageRenditionField


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    code_siigo = serializers.IntegerField()
    name = serializers.CharField()
    iva = serializers.IntegerField()
    description = serializers.CharField()
    cantidad = serializers.IntegerField()
    precio = serializers.DecimalField(decimal_places=2, max_digits=9)
    cover_image = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    def get_images(self, blocks):
        images = []
        for image in blocks.images:
            images.append(ImageRenditionField("fill-100x100").to_representation(image.value))
        return images

    def get_cover_image(self, blocks):
        if blocks.cover_image:
            cover = blocks.cover_image[0].value
            return ImageRenditionField("fill-100x100").to_representation(cover)
        return None
