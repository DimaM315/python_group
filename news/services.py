from .models import NewsStore, Category_News


def get_news_for_category(category_id):
	""" Возвращает все новости по заданной категории """
	news = NewsStore.objects.filter(category=category_id).all()
	
	return news