from django.contrib import admin
from .models import Role, Worker, Student
# Register your models here.
@admin.register(Role)
class Role(admin.ModelAdmin):
    list_display = ('name', 'status',)
    list_editable = ('status',)
    
@admin.register(Worker)
class Worker(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'status',)
    list_filter = ('status', 'role',)
    list_editable = ('status', 'role',)
    
@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ('full_name', 'field', 'day', 'time', 'status',)
    list_filter = ('status', 'field', 'day', 'time',)
    list_editable = ('status', 'field', 'day', 'time',)