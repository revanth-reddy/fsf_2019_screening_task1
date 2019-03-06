from django.contrib import admin
from .models import Task, Team


admin.site.register(Team)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','created_by', 'team', 'assignee', 'status', 'created_at', 'last_modified']

admin.site.register(Task, TaskAdmin)