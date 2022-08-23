from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='article_index'),
    path('<str:article_id>', article_page, name='article_page')
]
