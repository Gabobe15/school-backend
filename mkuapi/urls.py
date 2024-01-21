from rest_framework import routers
from .views import StudentsViewSet,StudentInActiveSet
from django.urls import path, include
# from . import views


router = routers.DefaultRouter()
# url, views, name 
router.register('students', StudentsViewSet, 'students')
router.register('inactive',StudentInActiveSet , 'students')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('students/', StudentsViewSet.as_view()),
# ]