from django.shortcuts import render, get_object_or_404

from tasks.models import Task

def index(request):
    latest_tasks_list = Task.objects.order_by('date')[:5]
    context = {
        'latest_tasks_list': latest_tasks_list
    }
    return render(request, 'tasks/index.html', context)

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail.html', {'task': task})
