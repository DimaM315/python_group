from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='feed_index'),
    path('get_contents', get_contents, name='get_contents')
]