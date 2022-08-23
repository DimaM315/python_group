from django import template
from django.shortcuts import get_object_or_404


import feed.services as services

register = template.Library()


@register.inclusion_tag('feed/content_container.html')
def get_feed_content():
	blocks_content = []
	for _ in range(3):
		blocks_content.append(
				services.get_random_one_mem_and_watchcode()
			)

	return {'blocks_content': blocks_content}



@register.inclusion_tag('feed/news_recomm.html')
def get_news_recomm():
	pass