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
