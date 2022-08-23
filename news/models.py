from django.db import models
from django.urls import reverse


class NewsStore(models.Model):
    title = models.CharField(unique=True, max_length=100,
                             db_index=True, verbose_name='Загаловок')

    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category_News',
                                 on_delete=models.PROTECT,
                                 null=True,
                                 verbose_name='Категория')

    # blank=True разрешает оставить пустым
    # auto_now=True записывает в поле текущую дату и время
    # on_delete=models.PROTECT - 
    # ограничение на удаление внешнего ключа, если на него есть ссылки

    def get_absolute_url(self):
        # первый пар-т имя маршрута из файла urls
        # второй - словарь параметров запроса которые связаны с моделью
        return reverse('news_page', kwargs={'news_id': self.pk})

    def __repr__(self):
        return "<News obj: {0}>".format(self.title)

    class Meta:
        verbose_name = 'Новость'  # наименование в ед.числе
        verbose_name_plural = 'Новости'  # наименование в мн.числе
        ordering = ['-created_at']  # - в начале, сортирует в обратном порядке


class Category_News(models.Model):
    title = models.CharField(unique=True, max_length=100,
                             db_index=True, verbose_name='Загаловок')

    def get_absolute_url(self):
        return reverse('news_category_page', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']



# после создания модели, создаём миграцию: python manage.py makemigrations
# приминяем миграцию python manage.py migrate


# Работа с таблицей.

# 1) Переходим в django shell - python manage.py shell
# 2) Импортируем модель: from news.models import News

# 	Create
# 	 news1 = News(title="News#1", content="Some contents")
#	 Сохраняем: news1.save()
#	 или создать (без .save()): News.objects.create(title='', content='') / News.objects.get_or_create(...)

    # Чтобы добавить несколько записей в ManyToManyField за один раз
    # model_name.field_name.add(john, paul, george, ringo)

#	Get
#		news = News.objects.all()
#		one_news = News.objects.get(id=1)

#	Update
#		news = News.objects.filter(title='Some').first()
#		news.title = 'Some else'
#		news.save()

#	Delete
#		news = News.objects.get(id=1)
#		news.delete()
