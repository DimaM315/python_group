from django.contrib import admin

from .models import Tasks


class TasksConfig(admin.ModelAdmin):
	list_display = ('id', 'text', 'level')
	list_display_links = ('id', 'text')
	search_fields = ('text', 'level')


admin.site.register(Tasks, TasksConfig)