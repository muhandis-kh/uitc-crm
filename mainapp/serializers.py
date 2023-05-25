from rest_framework import serializers

from .models import Branch, Room, Group

""" Admin panel uchun CRUD Serializers """
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Branch
        fields = ('__all__')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('__all__')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields  =('__all__')

class BranchAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id', 'name', 'adress')

class RoomAPISerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.name')
    class Meta:
        model = Room
        fields = ('id', 'number', 'capacity', 'branch', 'branch_name')

class GroupAPISerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.name')
    field_name = serializers.CharField(source='field.name')
    teacher_name = serializers.CharField(source='teacher.full_name')
    room_name = serializers.CharField(source='room.slug')
    
    class Meta:
        model = Group
        fields = ('id', 'branch', 'branch_name', 'field', 'field_name', 'name', 'room', 'room_name', 'teacher', 'teacher_name', 'day', 'time')
