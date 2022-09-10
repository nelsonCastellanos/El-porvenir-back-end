from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.settings.models import BaseSetting, register_setting
from .field_block import NativeColorBlock


class HomePage(Page):
    slider = StreamField([
        ('image', ImageChooserBlock()),
    ], use_json_field=True, collapsed=True)


    body = StreamField([
        ('section', blocks.StreamBlock([
            ('ancho', blocks.IntegerBlock()),
            ('descripcion', blocks.CharBlock()),
            ('imagen', ImageChooserBlock()),
        ])),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('slider'),
        FieldPanel('body'),
    ]



@register_setting
class WebsiteSettings(BaseSetting):
    vat = models.CharField(max_length=16, help_text=('Your company VAT with initial state code (i.e.: GB)'))
    phone = models.CharField(max_length=16, help_text=('Your company phone number'))
    email = models.EmailField(max_length=255, help_text=('Your company email address'))

    facebook = models.URLField(help_text=('Your Facebook page URL'))
    instagram = models.URLField(help_text=('Your Instagram page URL'))
    pinterest = models.URLField(help_text=('Your Pinterest page URL'))

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('vat'),
                FieldPanel('phone'),
                FieldPanel('email'),
            ],
            heading=('Company information'),
            classname='collapsible',
        ),
        MultiFieldPanel(
            [
                FieldPanel('facebook'),
                FieldPanel('instagram'),
                FieldPanel('pinterest'),
            ],
            heading=('Social media'),
            classname='collapsible',
        ),
    ]


@register_setting
class AnalyticsSettings(BaseSetting):
    google_analytics = models.CharField(null=True, blank=True, max_length=15, help_text=('Google Analytics tracking ID'))

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('google_analytics'),
            ],
            heading=('Tracking'),
            classname='collapsible',
        ),
    ]