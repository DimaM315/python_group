import random

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import feed.services as services


def index(request):
	context = {
		'title': 'Главная', 
	}
	return render(request, 'feed/index.html', context)


def get_contents(request):
	mem, watch_code = services.get_random_one_mem_and_watchcode()

	return JsonResponse({
				"mem_img_url": mem.photo.url, 
				"mem_text_on_photo": mem.text_on_photo, 
				"watch_code_question": watch_code.question,
				"watch_code_answer": watch_code.answer,
			})
