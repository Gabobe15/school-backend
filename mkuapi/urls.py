from django.urls import path
from .import views



urlpatterns = [
    path('inactive/', views.InactiveListView.as_view(), name='inactive-student'),
    path('students/', views.StudentListView.as_view(), name='students'),
    # path('register/', views.RegisterStudent.as_view(), name='register'),
    path('single-student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('update-student/<int:pk>/', views.UpdateStudentView.as_view(), name='update-student'),

]


# from rest_framework import routers
# from .views import StudentsViewSet,StudentInActiveSet

# router = routers.DefaultRouter()
# # url, views, name 
# router.register('students/<int:pk>/', StudentsViewSet, 'students')
# router.register('inactive',StudentInActiveSet , 'students')

# urlpatterns = [
#     path('students/', StudentsViewSet.as_view()),
# ]