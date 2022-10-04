from wagtail.blocks import ChooserBlock
from functools import cached_property
from category.models import Category
from generic_chooser.widgets import AdminChooser
from django.urls import reverse
from django.contrib.admin.utils import quote


class CategoryChooser(AdminChooser):
    choose_one_text = 'Choose a Category'
    choose_another_text = 'Choose another Category'
    link_to_chosen_text = 'Edit this Category'
    model = Category
    choose_modal_url_name = 'category_chooser:choose'

    def get_edit_item_url(self, item):
        return reverse('wagtailsnippets:edit', args=('base', 'category', quote(item.pk)))

class CategoryChooserBlock(ChooserBlock):
    @cached_property
    def target_model(self):
        return Category

    @cached_property
    def widget(self):
        return CategoryChooser()

    def get_form_state(self, value):
        return self.widget.get_value_data(value)