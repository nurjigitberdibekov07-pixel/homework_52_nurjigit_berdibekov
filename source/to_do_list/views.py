from django.shortcuts import render
from django.http import HttpResponseRedirect

from to_do_list.models import Task


# Create your views here.
def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, "tasks.html", context)

def add(request):
    if request.method == 'GET':
        return render(request, 'new_task.html', {
            'status_choices': Task.STATUS_CHOICES })
    elif request.method == 'POST':
            Task.objects.create(
                content=request.POST.get('content'),
                status=request.POST.get('status', 'new'),
                due_date=request.POST.get('due_date') or None,
            )
            return HttpResponseRedirect("/tasks")

def delete(request):
    id = request.GET.get('id')

    if id:
        task = Task.objects.get(id=int(id))
        task.delete()
        return HttpResponseRedirect("/tasks")
