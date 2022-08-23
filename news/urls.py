from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='news_index'),
    path('category/<int:category_id>', category_page, name='news_category_page'),
    path('<str:news_id>', NewsDetail.as_view(), name='news_page'),
    path("get_news_json/<int:news_id>", delete_news),
]
# поле name, необходима для ссылак, ссылаемся на значение name