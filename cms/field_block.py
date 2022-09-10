from wagtail.blocks import FieldBlock
from django.utils.functional import cached_property
from colorfield.fields import ColorField


class NativeColorBlock(FieldBlock):
    def __init__(self, **kwargs):
        self.field = ColorField()
        super().__init__(**kwargs)

    @cached_property
    def field(self):
        return ColorField()

    class Meta:
        icon = "radio-full"
