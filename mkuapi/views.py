from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, generics



class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# Create your views here. active users
class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [ permissions.AllowAny ] 
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']
    search_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']
    ordering_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']

    # queryset = Student.objects.all()
    queryset = Student.objects.filter(is_active=True).order_by('-id')


# Detail view
class StudentDetailView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ] 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    

# inActive model views
class StudentInActiveSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [ permissions.AllowAny ] 
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']
    search_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']
    ordering_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']

    # queryset = Student.objects.all()
    queryset = Student.objects.filter(is_active=False).order_by('-id')