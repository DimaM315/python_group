from django.db import models

class Memes(models.Model):
	"""
	Картинки с подписями на главной(feed) странице.
	"""
	photo = models.ImageField(upload_to='mems', blank=True) 
	text_on_photo = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


class WatchCode(models.Model):
	"""
	Блоки с вопросами "Какой результат этого кода" и сам код(2-5 строк).
	На главной(feed) странице.
	"""
	question = models.TextField()
	answer = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
	
		