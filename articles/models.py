from django.db import models
from django.urls import reverse


class Articles(models.Model):
    preview = models.ImageField(
        upload_to='articles_preview', blank=False, verbose_name='Картинка'
    )
    title = models.CharField(unique=True, max_length=100,
                             db_index=True, verbose_name='Загаловок')
    text = models.TextField(verbose_name='Текст статьи')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True)
    start_with_preview = models.BooleanField(default=True, verbose_name='Начало статьи-картинка?')


    def get_absolute_url(self):
        return reverse('article_page', kwargs={'article_id': self.pk})


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['id']
