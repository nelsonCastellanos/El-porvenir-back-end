from django.urls import path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.images import urls as wagtailimages_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)


urlpatterns = [
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('images/', include(wagtailimages_urls)),
    path('pages/', include(wagtail_urls)),
    path('api/v2/', api_router.urls),
]