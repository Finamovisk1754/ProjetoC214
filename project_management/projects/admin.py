from django.contrib import admin
from .models import Project, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'owner')
    search_fields = ('name', 'owner__username')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'due_date', 'completed')
    search_fields = ('name', 'project__name')
    list_filter = ('completed',)