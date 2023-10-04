from django.urls import path

from tasks.views import *

urlpatterns = [
    path('', index, name='index'),
    path('/add/', add, name='add'),
    path('/<int:task_id>/', detail, name='detail'),
    path('/uncomplete_task/<int:task_id>/', uncomplete_task, name='uncomplete_task'),
    path('/complete_task/<int:task_id>/', complete_task, name='complete_task'),
    path('/edit/<int:task_id>/', edit, name='edit'),
    path('/delete/<int:task_id>/', delete, name='delete')
]
