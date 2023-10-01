from django.shortcuts import render

from tasks.models import Task

def index(request):
    latest_tasks_list = Task.objects.order_by('date')[:5]
    context = {
        'latest_tasks_list': latest_tasks_list
    }
    return render(request, 'tasks/index.html', context)
