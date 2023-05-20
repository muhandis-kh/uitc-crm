from django.shortcuts import render
from pprint import pprint

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Branch, Room, Group
from .serializers import BranchSerializer, RoomSerializer, GroupSerializer

# Create your views here.

class BranchViewset(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [AllowAny]

    """ CRUD functions """
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
        except:
            return Response({'error':"Ma'lumotni olishda xatolik yuzaga keldi !!!"})
        try:
            new_branch = Branch.objects.create(
                name = data['name'],
                adress = data['adress'],
                status = data['status'],
            )
            new_branch.save()
            serializer = BranchSerializer(new_branch)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':"Ma'lumotni saqlashda xatolik yuzaga keldi !!!"}, 
                            status.HTTP_400_BAD_REQUEST)


