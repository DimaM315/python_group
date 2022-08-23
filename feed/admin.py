from django.contrib import admin

from .models import Memes, WatchCode


class MemesAdmin(admin.ModelAdmin):
	list_display = ('id', 'photo', 'text_on_photo', 'created_at')
	list_display_links = ('id',)
	search_fields = ('text_on_photo',)
	list_filter = ('created_at', )


class WatchCodeAdmin(admin.ModelAdmin):
	list_display = ('id', 'question', 'answer', 'created_at')
	list_display_links = ('id', 'question')
	search_fields = ('created_at',)


admin.site.register(WatchCode, WatchCodeAdmin)
admin.site.register(Memes, MemesAdmin)
