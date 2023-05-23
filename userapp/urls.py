from django.urls import path, include

from rest_framework import routers

from .views import WorkerViewset


router = routers.DefaultRouter()
router.register(r'worker', WorkerViewset, 'worker')

urlpatterns = [
    path('', include(router.urls)),
]


