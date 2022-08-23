from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


def zero_path(request):
	return HttpResponseRedirect(reverse('feed_index'))
	#return HttpResponse('hello world')


def not_found(request):
	return render(request, 'not_found.html')