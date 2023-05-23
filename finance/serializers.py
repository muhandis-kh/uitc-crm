from rest_framework.serializers import ModelSerializer
from .models import Expenses, Payment, Area, Income

class ExpensesSerializer(ModelSerializer):
    class Meta:
        model = Expenses
        fields = ('__all__')

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ('__all__')

class AreaSerializer(ModelSerializer):
    class Meta:
        model = Area
        fields = ('__all__')

class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = ('__all__')
