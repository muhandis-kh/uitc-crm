
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets

from .models import Worker, Field, Role, Student
from .serializers import WorkerSerializer, StudentSerializer, FieldSerializer, RoleSerializer

# Create your views here.
       
class WorkerViewset(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    def create(self, request, *args, **kwargs):
        request_data = request.data
        print(request_data)
        try:
            direction = Field.objects.get(id=request_data['direction'])
            role = Role.objects.get(id=request_data['role'])
            print(request_data)
        except Exception as e:
            return Response({f"Bunday yo'nalish yoki role topilmadi {e}"})
            print(e)
        status = request_data['status']
        try:
            new_worker = Worker.objects.create(
                direction=direction,
                role=role,
                full_name=request_data['full_name'],
                phone_number=request_data['phone_number'],
                passport=request_data['passport'],
                percentage=request_data['percentage'],
                salary=request_data['salary'],
                status=status.capitalize()
            )
            new_worker.save()
            serializer = WorkerSerializer(new_worker)
            return Response(serializer.data)
        except Exception as e:
            return Response({f"Ma'lumot saqlashda xatolik yuzaga keldi {e}"})
        
    def update(self, request, *args, **kwargs):
        data = self.get_object()
        request_data = request.data

        try: 
            if 'direction' in request_data:
                direction = Field.objects.get(id=request_data['direction'])
                role = Role.objects.get(id=request_data['role'])
        except:
            return Response({"Bunday filial topilmadi"})
            
        try:
            data.direction = direction if 'direction' in request_data else data.direction
            data.role = role if 'role' in request_data else data.role
            data.full_name = request_data['full_name'] if 'full_name' in request_data else data.full_name
            data.phone_number = request_data['phone_number'] if 'phone_number' in request_data else data.phone_number
            data.passport = request_data['passport'] if 'phone_number' in request_data else data.phone_number
            data.percentage = request_data['percentage'] if 'phone_number' in request_data else data.phone_number
            data.salary = request_data['salary'] if 'phone_number' in request_data else data.phone_number
            data.status = request_data['status'].capitalize() if 'status' in request_data else data.status
            data.save()
            
            serializer = WorkerSerializer(data)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({"Ma'lumot saqlashda xatolik yuzaga keldi"})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({"Ma'lumot o'chirildi"})

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
class FieldViewset(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
class RoleViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'