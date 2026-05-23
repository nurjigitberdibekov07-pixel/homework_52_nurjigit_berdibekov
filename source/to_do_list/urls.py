from django.urls import path

from django.urls import path
from .views import tasks

urlpatterns = [
    path('tasks/', tasks, name='task_list'),
    # path('create/', views.task_create, name='task_create'),
]
