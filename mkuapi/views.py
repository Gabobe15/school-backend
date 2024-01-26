from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class StudentListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination
    
     # fields = ['id','regno', 'fullname', 'course', 'email', 'contact', 'is_active']
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['regno', 'fullname', 'course', 'email', 'contact']
    search_fields = ['regno', 'fullname', 'course', 'email', 'contact']
    ordering_fields = ['regno', 'fullname', 'course', 'email', 'contact']
    # queryset = Student.objects.filter(is_active=True).order_by('-id')
    
    def get_queryset(self, *args, **kwargs):
        std = Student.objects.filter(is_active=True).order_by('-id')

        # Role Filters
        role = self.request.query_params.get('role',None)

        if role:
            std = std.filter(role=role)

        return std
    
    
class InactiveListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination
    
     # fields = ['id','regno', 'fullname', 'course', 'email', 'contact', 'is_active']
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['regno', 'fullname', 'course', 'email', 'contact']
    search_fields = ['regno', 'fullname', 'course', 'email', 'contact']
    ordering_fields = ['regno', 'fullname', 'course', 'email', 'contact']
    queryset = Student.objects.filter(is_active=False).order_by('-id')



# Detail view
class StudentDetailView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ] 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer   

# class RegisterStudent(generics.GenericAPIView):
#     permission_classes = [
#         permissions.AllowAny,
#     ] 

#     serializer_class = RegisterStudentSerializer
           
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         email = request.data['email']
#         student = Student.objects.filter(email=email).exists()
#         if student:
#             raise AuthenticationFailed('Email already exists!')
#         else:
#             student = serializer.save()

#             return Response({
#                 "student": StudentSerializer(student,
#                 context=self.get_serializer_context()).data, 
#             })

# Update user
class UpdateStudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny,]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)














# Create your views here. active users
# class StudentsViewSet(viewsets.ModelViewSet):
#     serializer_class = StudentSerializer
#     permission_classes = [ permissions.AllowAny ] 
#     pagination_class = CustomPageNumberPagination
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']
#     search_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']
#     ordering_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']

#     # queryset = Student.objects.all()
#     queryset = Student.objects.filter(is_active=True).order_by('-id')


 

# inActive model views
# class StudentInActiveSet(viewsets.ModelViewSet):
#     serializer_class = StudentSerializer
#     permission_classes = [ permissions.AllowAny ] 
#     pagination_class = CustomPageNumberPagination
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']
#     search_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']
#     ordering_fields = ['regno','fullname', 'course', 'email', 'contact', 'is_active']

#     # queryset = Student.objects.all()
#     queryset = Student.objects.filter(is_active=False).order_by('-id')