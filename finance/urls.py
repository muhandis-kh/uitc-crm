from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpensesViewsets, PaymentViewsets, AreaViewsets, \
    IncomeViewsets,ExpensesAPIViewsets, PaymentAPIViewsets, AreaAPIViewsets, \
        IncomeAPIViewsets

router = DefaultRouter()
router.register(r'expenses', ExpensesViewsets, 'expenses')
router.register(r'payment', PaymentViewsets, 'payment')
router.register(r'area', AreaViewsets, 'area')
router.register(r'income', IncomeViewsets, 'income')

router.register(r'expenses-api', ExpensesAPIViewsets, 'expenses-api')
router.register(r'payment-api', PaymentAPIViewsets, 'payment-api')
router.register(r'area-api', AreaAPIViewsets, 'area-api')
router.register(r'income-api', IncomeAPIViewsets, 'income-api')

urlpatterns = [
    path('', include(router.urls)),
]

