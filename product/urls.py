
from django.urls import re_path

from product.views import ProductListView

urlpatterns = [
    re_path('^products', ProductListView.as_view()),
]

