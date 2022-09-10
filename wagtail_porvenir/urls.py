from django.urls import path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.images import urls as wagtailimages_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from .api import api_router


urlpatterns = [
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('images/', include(wagtailimages_urls)),
    path('pages/', include(wagtail_urls)),
    path('api/v2/', api_router.urls),
]