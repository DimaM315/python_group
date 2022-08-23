from django.shortcuts import render


def index(request, level=1):
	context = {
		'title': 'Задачи',
		'tasks_level': level
	}
	return render(request, 'tasks/index.html', context)
