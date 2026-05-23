from django.shortcuts import render

from to_do_list.models import Task


# Create your views here.
def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, "tasks.html", context)