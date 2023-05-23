from django.urls import path, include

from rest_framework import routers

from .views import ExpencesViewSet, PaymentViewSet, AreaViewSet, IncomeViewSet

router = routers.DefaultRouter()
router.register(r'expences', ExpencesViewSet)
router.register(r'payment', PaymentViewSet)
router.register(r'area', AreaViewSet)
router.register(r'Income', IncomeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
