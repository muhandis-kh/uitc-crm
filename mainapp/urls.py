from django.urls import path, include

from rest_framework import routers

from .views import BranchViewset, RoomViewset, GroupViewset


router = routers.DefaultRouter()
router.register(r'branch', BranchViewset, 'branch')
router.register(r'room', RoomViewset, 'room')
router.register(r'group', GroupViewset, 'group')

urlpatterns = [
    path('', include(router.urls)),
]


