from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task, ResponseFile
from django.contrib.auth.models import User
from .forms import TaskForm, UserForm, ProjectForm, ResponseFileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import TaskForm
from .forms import TaskResponseForm
import os 
from django.conf import settings

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = UserCreationForm()
    return render(request, 'projects/register.html', {'form': form})

@login_required
def home_page(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/home.html', {'projects': projects})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  # Adicione request.FILES para lidar com o upload de arquivos
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, 'Projeto criado com sucesso!')
            return redirect('project_detail', project_id=project.id)
        else:
            messages.error(request, 'Erro ao criar projeto. Por favor, corrija os campos abaixo.')
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})


@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('home')
    return render(request, 'projects/delete_project.html', {'project': project})

@login_required
def create_task(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', project_id=project_id)
    else:
        form = TaskForm()
    return render(request, 'projects/create_task.html', {'form': form, 'project': project})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project_id = task.project.id
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('project_detail', project_id=project_id)
    return render(request, 'projects/delete_task.html', {'task': task})

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.tasks.all()
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})

@login_required
def upload_task_response(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskResponseForm(request.POST, request.FILES)
        if form.is_valid():
            response = form.save(commit=False)
            response.task = task
            response.save()
            messages.success(request, 'Upload concluído com sucesso!')
            return redirect('upload_task_response', task_id=task.id)
        else:
            messages.error(request, 'Erro ao fazer upload da resposta. Por favor, corrija os campos abaixo.')
    else:
        form = TaskResponseForm()
    responses = task.responses.all()
    return render(request, 'projects/upload_task_response.html', {'form': form, 'task': task, 'responses': responses})

@login_required
def delete_task_response(request, response_id):
    response = get_object_or_404(ResponseFile, id=response_id)
    task_id = response.task.id
    response.delete()
    messages.success(request, 'Resposta excluída com sucesso!')
    return redirect('upload_task_response', task_id=task_id)

@login_required
def view_task_response(request, response_id):
    response = get_object_or_404(ResponseFile, id=response_id)
    file_path = os.path.join(settings.MEDIA_ROOT, response.file.name)
    file_content = None

    if response.file.name.endswith('.txt'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
        except IOError:
            file_content = "Não foi possível ler o conteúdo do arquivo."
    else:
        file_content = "Visualização de arquivos disponível apenas para arquivos de texto (.txt)."

    return render(request, 'projects/view_task_response.html', {'response': response, 'file_content': file_content})
