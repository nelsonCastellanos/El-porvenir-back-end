from wagtail.core import hooks

from category.views import CategoryChooserViewSet

@hooks.register('register_admin_viewset')
def register_person_chooser_viewset():
    return CategoryChooserViewSet('category_chooser', url_prefix='category-chooser')