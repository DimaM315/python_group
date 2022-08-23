from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='tasks_index'),
    path("level/<int:level>", index, name="task_with_level")
]