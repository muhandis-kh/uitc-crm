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