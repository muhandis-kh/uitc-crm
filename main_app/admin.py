from django.contrib import admin
from .models import Branch, Field, Room
# Register your models here.

@admin.register(Branch)
class Branch(admin.ModelAdmin):
    list_display = ("name", 'id', 'address', 'slug', 'status', 'created_at',)
    list_filter = ('status', 'created_at',)
    list_editable = ('status',)

@admin.register(Field)
class Field(admin.ModelAdmin):
    list_display = ('name', 'id', 'cost', 'duration', 'slug', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'duration')
    list_editable = ('status',)

@admin.register(Room)
class Room(admin.ModelAdmin):
    list_display = ('number', 'id', 'branch', 'capacity', 'slug', 'status', 'created_at')
    list_filter = ('branch', 'capacity', 'status', 'created_at')
    list_editable = ('status',)