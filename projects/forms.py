from django import forms
from django.contrib.auth.models import User
from .models import Project, ResponseFile
from .models import Task, TaskResponse

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'completed']

class TaskResponseForm(forms.ModelForm):
    class Meta:
        model = TaskResponse
        fields = ['file']
 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email'] 


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description'] 

class ResponseFileForm(forms.ModelForm):
    class Meta:
        model = ResponseFile
        fields = ['file'] 
