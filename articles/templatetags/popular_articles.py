from django import template
from django.shortcuts import get_object_or_404


from articles.models import Articles

register = template.Library()


@register.inclusion_tag('articles/popular_articles_recomm.html')
def get_popular_articles_recomm():
	articles = Articles.objects.all()[0:6]
	return {'articles': articles}