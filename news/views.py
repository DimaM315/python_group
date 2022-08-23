from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

# чтобы получить настройки проекта 
from django.conf import settings

from .models import NewsStore, Category_News
from .services import *


def index(request):
	context = {
		'title': 'Новости', 
	}

	#return HttpResponse('hello world')
	return render(request, 'news/index.html', context)


def category_page(request, category_id):
	current_category = Category_News.objects.filter(id=category_id).first()

	all_category = Category_News.objects.all()
	
	context = {
		'news': get_news_for_category(category_id), 
		'title': current_category.title, 
		'categoties': all_category
	}

	#return HttpResponse('category - '+ category.title + '\nНовость: ' + news[0].title)
	return render(request, 'news/index.html', context)


def delete_news(request, news_id):
	# request.GET request.POST - словари в которых храняться переданные параметры запроса
	# print(request.GET, request.POST)
	return JsonResponse({"response_text": "success delete news with id " + str(news_id)})





class NewsDetail(View):
	def get(self, request, news_id):
		#print('\n', dir(self), '\n')
		#return HttpResponse('<h1>' + news_id + '</h1>')
		news = NewsStore.objects.get(id=news_id)
		return render(request, 'news/single_news.html', {"news": news})
