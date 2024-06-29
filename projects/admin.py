# admin.py
from django.contrib import admin
from .models import Project, ResponseFile, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner', 'created_at', 'updated_at')

@admin.register(ResponseFile)
class ResponseFileAdmin(admin.ModelAdmin):
    list_display = ('project', 'file', 'uploaded_at')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project', 'created_at', 'updated_at', 'completed')
    list_filter = ('project', 'completed')
