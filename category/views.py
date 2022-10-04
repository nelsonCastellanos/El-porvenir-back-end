from django.shortcuts import render
from category.models import Category
from generic_chooser.views import ModelChooserViewSet

# Create your views here.

class CategoryChooserViewSet(ModelChooserViewSet):
    icon = 'user'
    model = Category
    page_title = "Choose a category"
    per_page = 10
    order_by = 'name'
    fields = ['name', 'description']