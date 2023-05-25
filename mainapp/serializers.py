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
        fields = ('id', 'name', 'adress', 'slug')

class RoomAPISerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.name')
    # branch_adress = serializers.CharField(source='branch.adress')
    # branch_status = serializers.BooleanField(source='branch.status')
    # branch_created_at = serializers.DateTimeField(source='branch.created_at')
    class Meta:
        model = Room
        fields = ('id', 'number', 'capacity', 'branch_name', 'slug')

class GroupAPISerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.name')
    field_name = serializers.CharField(source='field.name')
    teacher_name = serializers.CharField(source='teacher.full_name')
    room = serializers.IntegerField(source='room.number')

    class Meta:
        model = Group
        fields = ('id', 'branch_name', 'field_name', 'name', 'room', 'teacher_name', 'day', 'time', 'slug')
