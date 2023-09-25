from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(null=True)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
