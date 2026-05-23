from django.contrib import admin
from .models import CustomUser, Project, Task

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role',)
    search_fields = ('username', 'email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'priority', 'status', 'due_date', 'created_by')
    list_filter = ('priority', 'status', 'project')
    search_fields = ('title',)