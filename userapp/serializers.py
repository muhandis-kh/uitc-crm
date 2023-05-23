from rest_framework import serializers

from .models import Worker

""" Admin panel uchun CRUD Serializers """
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Worker
        fields = ('__all__')
