from django.urls import path
from .views import tasks, add, delete

urlpatterns = [
    path('tasks/', tasks),
    path('tasks/add/', add),
    path('tasks/delete/', delete),
]
