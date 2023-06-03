from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Field, Role, Worker, Student
from .serializers import FieldSerializer, RoleSerializer, WorkerSerializer, StudentSerializer,\
    FieldAPISerializer, WorkerAPISerializer, RoleAPISerializer, StudentAPISerializer

# Create your views here.

""" CRUD API """
class FieldViewset(ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    filterset_fields = ['name', 'status', 'students__full_name']

class RoleViewset(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    filterset_fields = ['name', 'status']

class WorkerViewset(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    filterset_fields = ['full_name', 'status']

class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    filterset_fields = ['full_name', 'time', 'day', 'phone_number', 'father_name', 'status']

""" API """
class FieldAPIViewset(ModelViewSet):
    queryset = Field.objects.filter(status=True)
    serializer_class = FieldAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class RoleAPIViewset(ModelViewSet):
    queryset = Role.objects.filter(status=True)
    serializer_class = RoleAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class WorkerAPIViewset(ModelViewSet):
    queryset = Worker.objects.filter(status=True)
    serializer_class = WorkerAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class StudentAPIViewset(ModelViewSet):
    queryset = Student.objects.filter(status=True)
    serializer_class = StudentAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
