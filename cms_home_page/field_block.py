from wagtail.blocks import FieldBlock
from colorfield.fields import ColorField

class ColorFieldBlock(FieldBlock):
    def __init__(self, **kwargs):
        self.field = ColorField(**kwargs).formfield()
        super().__init__(**kwargs)

    class Meta:
        icon = "radio-full"
