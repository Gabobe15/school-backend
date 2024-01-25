from rest_framework import routers
from .views import StudentsViewSet,StudentInActiveSet
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
# url, views, name 
router.register('students/<int:pk>/', StudentsViewSet, 'students')
router.register('inactive',StudentInActiveSet , 'students')

urlpatterns = [
    path('', include(router.urls)),
    path('single-student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),

]

# urlpatterns = [
#     path('students/', StudentsViewSet.as_view()),
# ]