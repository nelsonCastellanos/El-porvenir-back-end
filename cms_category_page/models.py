from wagtail.api import APIField
from wagtail.blocks import PageChooserBlock, StructBlock, CharBlock, ChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from category.blocks import CategoryChooserBlock
from cms_category_page.serializer import CategoryPageCategoryBlockSerializer


class CategoryPageCategoryBlock(StructBlock):
    titulo = CharBlock()
    imagen = ImageChooserBlock()
    pagina = PageChooserBlock(label="page", required=False)
    category = CategoryChooserBlock()

    def get_api_representation(self, value, context=None):
        serializer = CategoryPageCategoryBlockSerializer(value)
        return serializer.data

    class Meta:
        icon = 'user'
        form_classname = 'formset struct-block'


class CategoryPage(Page):
    categoria = StreamField([
        ('categoria', CategoryPageCategoryBlock())
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('categoria'),
    ]

    # export fields over the api
    api_fields = [
        APIField('categoria'),
    ]
