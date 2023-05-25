from rest_framework import serializers

from .models import Worker, Field, Role, Student

""" Admin panel uchun CRUD Serializers """
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Worker
        fields = ('__all__')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('__all__')
        
class StudentSerializer(serializers.ModelSerializer):
    field_name = serializers.CharField(source='field.name')
    class Meta:
        model = Student
        fields = ('__all__')
        read_only_fields = (
            'field_name',
        )

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('__all__')
        
    """ API """
    
class WorkerAPISerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.name')
    direction_name = serializers.CharField(source='direction.name')
    
    class Meta:
        model = Worker
        fields= ('id', 'full_name', 'phone_number', 'passport', 'percentage', 'salary', 'role_name', 'direction_name', 'slug')
        
class StudentAPISerializer(serializers.ModelSerializer):
    field_name = serializers.CharField(source='field.name')
    class Meta:
        model = Student
        fields = ('id', 'slug', 'full_name', 'phone_number', 'passport', 'date_of_birth', 'father_name', 'father_phone', 'field_name', 'time', 'day')        