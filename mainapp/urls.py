from django.urls import path, include

from rest_framework import routers

from .views import BranchViewset, GroupViewset,  RoomViewset, \
                    BranchAPIListview, RoomAPIListview, GroupAPIListview,\
                        BranchAPIDetailview, RoomAPIDetailview, GroupAPIDetailview

router = routers.DefaultRouter()
router.register(r'branch', BranchViewset, 'branch')
router.register(r'room', RoomViewset, 'room')
router.register(r'group', GroupViewset, 'group')

urlpatterns = [
    path('', include(router.urls)),
    # path('branch-api/<int:id>/', BranchAPIDetailview.as_view()),
    path('branch-api/<slug:slug>/', BranchAPIDetailview.as_view()),
    path('branch-api', BranchAPIListview.as_view()),
    path('room-api/<slug:slug>/', RoomAPIDetailview.as_view()),
    path('room-api', RoomAPIListview.as_view()),
    path('group-api/<slug:slug>/', GroupAPIDetailview.as_view()),
    path('group-api', GroupAPIListview.as_view()),
]


