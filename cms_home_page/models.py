from colorfield.fields import ColorField
from wagtail.blocks import FieldBlock, PageChooserBlock
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from cms_home_page.field_block import ColorFieldBlock


class HomePageSectionBlock(blocks.StructBlock):
    ancho = blocks.IntegerBlock()
    descripcion = blocks.RichTextBlock()
    imagen = ImageChooserBlock()
    page = PageChooserBlock(label="page", required=False)
    color = ColorFieldBlock(default="#000000")

    class Meta:
        icon = 'user'
        form_classname = 'formset struct-block'


class HomePageSlideBlock(blocks.StructBlock):
    imagen = ImageChooserBlock()
    pagina = PageChooserBlock(label="page", required=False)

    class Meta:
        icon = 'house'
        form_classname = 'formset struct-block'


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
