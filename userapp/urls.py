from django.urls import path, include

from rest_framework import routers

from .views import WorkerViewset, FieldViewset, StudentViewset, RoleViewset


router = routers.DefaultRouter()
router.register(r'worker', WorkerViewset, 'worker')
router.register(r'field', FieldViewset, 'field')
router.register(r'student', StudentViewset, 'student')
router.register(r'role', RoleViewset, 'role')


urlpatterns = [
    path('', include(router.urls)),
]


