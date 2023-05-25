from django.urls import path, include

from rest_framework import routers

from .views import (FieldViewset, RoleViewset, StudentDetailview, StudentListview, StudentViewset, WorkerDetailview,
    WorkerListview, WorkerViewset)


router = routers.DefaultRouter()
router.register(r'worker', WorkerViewset, 'worker')
router.register(r'field', FieldViewset, 'field')
router.register(r'student', StudentViewset, 'student')
router.register(r'role', RoleViewset, 'role')


urlpatterns = [
    path('', include(router.urls)),
    path('worker-api/<slug:slug>', WorkerDetailview.as_view()),
    path('worker-api', WorkerListview.as_view()),
    path('student-api/<slug:slug>', StudentDetailview.as_view()),
    path('student-api', StudentListview.as_view()),
]


