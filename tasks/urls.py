from django.urls import path

from tasks.views import *

urlpatterns = [
    path('', index, name='index'),
    path('/<int:task_id>/', detail, name='detail')
]
