from django.shortcuts import render
from django.shortcuts import get_object_or_404


from .models import Articles


def index(request):
	context = {
		'title': 'Статьи', 
	}
	return render(request, 'articles/index.html', context)


def article_page(request, article_id):
	article = get_object_or_404(Articles, pk=article_id)

	context = {
		'article': article
	}
	return render(request, 'articles/single_aricle.html', context)
