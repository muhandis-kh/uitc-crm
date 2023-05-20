from django.urls import path, include

from rest_framework import routers

from .views import BranchViewset


router = routers.DefaultRouter()
router.register(r'branch', BranchViewset, 'branch')

urlpatterns = [
    path('', include(router.urls)),
]


