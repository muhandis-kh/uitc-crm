from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FieldViewset, RoleViewset, WorkerViewset, StudentViewset, \
    FieldAPIViewset, RoleAPIViewset, WorkerAPIViewset, StudentAPIViewset

router = DefaultRouter()
router.register(r'field', FieldViewset, 'fieldset')
router.register(r'role', RoleViewset, 'role')
router.register(r'worker', WorkerViewset, 'worker')
router.register(r'student', StudentViewset, 'student')
router.register(r'field-api', FieldAPIViewset, 'field-api')
router.register(r'role-api', RoleAPIViewset, 'role-api')
router.register(r'worker-api', WorkerAPIViewset, 'worker-api')
router.register(r'student-api', StudentAPIViewset, 'student-api')

urlpatterns = [
    path('', include(router.urls))
]

