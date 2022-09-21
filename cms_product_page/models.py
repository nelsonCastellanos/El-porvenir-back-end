from wagtail.api import APIField
from wagtail.blocks import PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks

from cms_product_page.serializer import ProductPageCategoryBlockSerializer


class ProductPageCategoryBlock(blocks.StructBlock):
    titulo = blocks.CharBlock()
    imagen = ImageChooserBlock()
    pagina = PageChooserBlock(label="page", required=False)

    def get_api_representation(self, value, context=None):
        serializer = ProductPageCategoryBlockSerializer(value)
        return serializer.data

    class Meta:
        icon = 'user'
        form_classname = 'formset struct-block'


class ProductPage(Page):
    categoria = StreamField([
        ('categoria', ProductPageCategoryBlock())
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('categoria'),
    ]

    # export fields over the api
    api_fields = [
        APIField('categoria'),
    ]
