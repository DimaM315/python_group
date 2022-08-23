from django import template
from django.shortcuts import get_object_or_404

from news.models import Category_News, NewsStore

register = template.Library()
# после создания тега нужно перезапустить приложение


@register.simple_tag()
def get_categories():
	c = get_object_or_404(Category_News)
	return Category_News.objects.all()




@register.inclusion_tag('news/categories_container.html')
def get_all_categories(page_title='undefind'):
	return {'categories': Category_News.objects.all(), 'page_title': page_title}


@register.inclusion_tag('inc/popular_news_recomm.html')
def get_popular_news_recomm():
	
	news = NewsStore.objects.all()[0:6]

	print('\n\n\n\n', news, '\n\n\n\n\n')
	return {'news': news}



@register.simple_tag()
def hello_custom_tag():
	return '<h1>Hello tag</h1>'