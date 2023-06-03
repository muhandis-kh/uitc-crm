from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Expenses, Payment, Area, Income
from .serializers import ExpensesSerializer, PaymentSerializer, IncomeSerializer, \
    AreaSerializer, ExpensesAPISerializer, PaymentAPISerializer, IncomeAPISerializer,\
        AreaAPISerializer

# Create your views here.

""" CRUD API """
class ExpensesViewsets(ModelViewSet):
    queryset =  Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes= [AllowAny]
    lookup_field = 'slug'

class PaymentViewsets(ModelViewSet):
    queryset =  Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes= [AllowAny]

class AreaViewsets(ModelViewSet):
    queryset =  Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes= [AllowAny]
    lookup_field = 'slug'

class IncomeViewsets(ModelViewSet):
    queryset =  Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes= [AllowAny]
    lookup_field = 'slug'

""" API """
class ExpensesAPIViewsets(ModelViewSet):
    queryset =  Expenses.objects.all()
    serializer_class = ExpensesAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class PaymentAPIViewsets(ModelViewSet):
    queryset =  Payment.objects.all()
    serializer_class = PaymentAPISerializer
    permission_classes= [AllowAny]

class AreaAPIViewsets(ModelViewSet):
    queryset =  Area.objects.all()
    serializer_class = AreaAPISerializer
    permission_classes= [AllowAny]
    lookup_field = 'slug'

class IncomeAPIViewsets(ModelViewSet):
    queryset =  Income.objects.all()
    serializer_class = IncomeAPISerializer
    permission_classes= [AllowAny]
    lookup_field = 'slug'

