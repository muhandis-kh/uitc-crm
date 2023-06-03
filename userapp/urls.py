from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FieldViewset, RoleViewset, WorkerViewset, StudentViewset, \
    FieldAPIViewset, RoleAPIViewset, WorkerAPIViewset, StudentAPIViewset

router = DefaultRouter()
router.register(r'field', FieldViewset)
router.register(r'role', RoleViewset)
router.register(r'worker', WorkerViewset)
router.register(r'student', StudentViewset)

router.register(r'field-api', FieldAPIViewset)
router.register(r'role-api', RoleAPIViewset)
router.register(r'worker-api', WorkerAPIViewset)
router.register(r'student-api', StudentAPIViewset)

urlpatterns = [
    path('', include(router.urls))
]

