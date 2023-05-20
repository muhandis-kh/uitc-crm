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


