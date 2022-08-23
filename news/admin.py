from django.contrib import admin

from .models import NewsStore, Category_News

class NewsAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', )#'category', 'created_at', 'updated_at')
	list_display_links = ('id', 'title')
	search_fields = ('title',) #'content') # поля по которым можно искать записи
	#list_filter = ('category', ) # поля по которым можно фильтровать


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'title',)
	list_display_links = ('id', 'title')
	search_fields = ('title',)


admin.site.register(NewsStore, NewsAdmin)
admin.site.register(Category_News, CategoryAdmin)

