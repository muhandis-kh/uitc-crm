from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Field, Role, Worker, Student

""" CRUD API """
class FieldSerializer(ModelSerializer):
    class Meta:
        model = Field
        fields = ('__all__')
        
class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ('__all__')

class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = ('__all__')

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')

""" API """
        

class WorkerAPISerializer(ModelSerializer):
    direction_name = serializers.CharField(source='diriction.name')
    direction_slug = serializers.CharField(source='diriction.slug')
    role_name = serializers.CharField(source='role.name')
    role_slug = serializers.CharField(source='role.slug')
    class Meta:
        model = Worker
        fields = ('id', 'full_name', 'slug', 'phone_number', 'passport', 'percentage', 'salary',\
                  'direction_name', 'direction_slug', 'role_name', 'role_slug')

class RoleAPISerializer(ModelSerializer):
    workers = WorkerAPISerializer(many=True, read_only = True)
    class Meta:
        model = Role
        fields = ('id', 'name', 'slug', 'workers')

class StudentAPISerializer(ModelSerializer):
    field_name = serializers.CharField(source='field.name')
    field_slug = serializers.CharField(source='field.slug')
    class Meta:
        model = Student
        fields = ('id', 'full_name', 'slug', 'date_of_birth', 'passport', 'phone_number', 'father_name', \
                  'father_phone', 'field_name', 'field_slug', 'day', 'time')

class FieldAPISerializer(ModelSerializer):
    students = StudentAPISerializer(many=True, read_only=True)
    workers = WorkerAPISerializer(many=True, read_only=True)
    class Meta:
        model = Field
        fields = ('id', 'name', 'slug', 'cost', 'duration', 'students', 'workers')
   




