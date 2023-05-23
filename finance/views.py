from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .models import Expenses, Payment, Area, Income
from .serializers import ExpensesSerializer, PaymentSerializer, AreaSerializer, IncomeSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class ExpencesViewSet(ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    