from wagtail.contrib.modeladmin.options import (
ModelAdmin, modeladmin_register)
from .models import Product


class ProductAdmin(ModelAdmin):
    model = Product
    

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(ProductAdmin)