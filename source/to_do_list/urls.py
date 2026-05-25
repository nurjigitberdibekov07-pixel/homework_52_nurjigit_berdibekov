from django.urls import path

from django.urls import path
from .views import tasks, add, delete

urlpatterns = [
    path('tasks/', tasks),
    path('tasks/add/', add),
    path('tasks/delete/', delete),
    # path('create/', views.task_create, name='task_create'),
]
