import random
from feed.models import Memes, WatchCode


def get_random_one_mem_and_watchcode():
	"""
	Возвращает кортеж из двух элементов. 1ый: объект mem, 2ой: объект watch_code.
	Причём достаётся объект со случайным pk
	"""
	memes_count = Memes.objects.count()
	watch_code_count = WatchCode.objects.count()
	return (
				Memes.objects.get(pk=random.randint(1, memes_count)),
				WatchCode.objects.get(pk=random.randint(1, watch_code_count)),
			)