from django.contrib import admin

from django.contrib import admin

from product.models import Product
from import_export.admin import ImportExportModelAdmin

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model = Product
        import_id_fields = ('code_siigo',)
        fields = ('code_siigo','name','iva','description','cantidad','precio','category__name')
    


admin.site.register(Product, ProductAdmin)