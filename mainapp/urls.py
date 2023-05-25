from django.urls import path, include

from rest_framework import routers

from .views import BranchViewset, RoomViewset, GroupViewset,\
                    BranchAPIListview, RoomAPIListview, GroupAPIListview


router = routers.DefaultRouter()
router.register(r'branch', BranchViewset, 'branch')
router.register(r'room', RoomViewset, 'room')
router.register(r'group', GroupViewset, 'group')

urlpatterns = [
    path('', include(router.urls)),
    path('branch-api', BranchAPIListview.as_view()),
    path('room-api', RoomAPIListview.as_view()),
    path('group-api', GroupAPIListview.as_view()),
]


