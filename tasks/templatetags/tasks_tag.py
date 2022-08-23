from django import template
from django.shortcuts import get_object_or_404

import random

from tasks.models import Tasks

register = template.Library()


@register.inclusion_tag('tasks/tasks_start_container.html')
def get_tasks_start(lvl=1):
	if lvl not in (1, 2, 3):
		print("get_tasks_start get unexpected par. lvl - " + str(lvl))
		lvl = 1

	tasks = Tasks.objects.filter(level=lvl)

	return {'tasks': tasks, 'tasks_lvl': lvl}




