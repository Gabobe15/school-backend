from django.urls import path, include
from .views import (
    FeesStructureView, 
    UpdateFeesView, 
    AddFees, 
    FeeDetailView, 
    StudentFeesView,
)

urlpatterns = [
    path('fees/', FeesStructureView.as_view(), name='fees'),
    path('update-fee/<int:pk>/', UpdateFeesView.as_view(), name='update-fee'),
    path('single-fee/<int:pk>/', FeeDetailView.as_view(), name='single-fee'),
    path('add-fee/', AddFees.as_view(), name="add-fee"),
    path('student-fees/<int:student>/', StudentFeesView.as_view(), name="student-fees"),
]
