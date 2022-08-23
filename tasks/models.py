from django.db import models

class Tasks(models.Model):
	class Lvls(models.IntegerChoices):
		first = 1
		second = 2
		fhird = 3


	text = models.TextField(blank=False, verbose_name='Текст задачи')
	answer = models.TextField(blank=False, verbose_name='Решение(стандартное)')
	answer_better = models.TextField(blank=False, verbose_name='Решение(better)')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
	

	level = models.IntegerField(choices=Lvls.choices, default=1, verbose_name="Уровень сложности")

	class Meta:
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'

	
	def __str__(self):
		return "Задача№" + str(self.id)