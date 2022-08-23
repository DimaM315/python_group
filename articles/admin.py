from django.contrib import admin

from .models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_filter = ('title', )


admin.site.register(Articles, ArticlesAdmin)

