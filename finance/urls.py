from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpensesViewsets, PaymentViewsets, AreaViewsets, \
    IncomeViewsets,ExpensesAPIViewsets, PaymentAPIViewsets, AreaAPIViewsets, \
        IncomeAPIViewsets

router = DefaultRouter()
router.register(r'expenses', ExpensesViewsets)
router.register(r'payment', PaymentViewsets)
router.register(r'area', AreaViewsets)
router.register(r'income', IncomeViewsets)

router.register(r'expenses-api', ExpensesAPIViewsets)
router.register(r'payment-api', PaymentAPIViewsets)
router.register(r'area-api', AreaAPIViewsets)
router.register(r'income-api', IncomeAPIViewsets)

urlpatterns = [
    path('', include(router.urls)),
]

