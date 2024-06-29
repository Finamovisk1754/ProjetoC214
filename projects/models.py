from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Project(models.Model):
    name = models.CharField(max_length=100)  # Campo de nome do projeto
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ResponseFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='response_files')
    file = models.FileField(upload_to='responses/')
    uploaded_at = models.DateTimeField(auto_now_add=True)    
    


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)  # Campo para indicar se a tarefa foi completada
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class TaskResponse(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='responses')
    file = models.FileField(upload_to='task_responses/')
    uploaded_at = models.DateTimeField(auto_now_add=True)    
