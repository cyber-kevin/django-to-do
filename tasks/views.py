from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

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

def add(request):
    if request.method == 'GET':
        return render(request, 'tasks/add.html')
    elif request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        body = request.POST.get('body', None)
        task = Task(title=title, body=body)
        task.save()
    
        return redirect('/tasks')

def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.completed = True
        task.save()

        return redirect('/tasks')

    return HttpResponse('Method not allowed', status=405)

def uncomplete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.completed = False
        task.save()

        return redirect('/tasks')

    return HttpResponse('Method not allowed', status=405)

def edit_body(request, task_id):
    new_body = request.POST[f'task{task_id}']

    task = Task.objects.get(pk=task_id)
    task.body = new_body
    task.save()

    return redirect('/tasks')

def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()

    return redirect('/tasks')
