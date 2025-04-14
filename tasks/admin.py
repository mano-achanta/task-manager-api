from django.contrib import admin
from .models import Task, CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'mobile')
    search_fields = ('username', 'email', 'mobile')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'task_type', 'status', 'created_at')
    list_filter = ('status', 'task_type')
    search_fields = ('name', 'description')