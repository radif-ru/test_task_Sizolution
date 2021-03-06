from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', cache_page(60 * 60 * 60)(views.index), name='index'),
]
