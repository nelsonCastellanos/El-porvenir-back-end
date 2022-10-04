from django.contrib import admin
from category.models import Category

from import_export.admin import ImportExportModelAdmin

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Category)