from django.shortcuts import render
from .models import FeesStructure
from .serializers import FeesStructureSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime,timedelta
# generics
from rest_framework import  permissions, generics

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    
class FeesStructureView(generics.ListAPIView):
    # queryset = Student.objects.all()
    
    serializer_class = FeesStructureSerializer
    permission_classes = [ permissions.AllowAny ] 
    pagination_class = CustomPageNumberPagination
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['regno','fees', 'payment', 'balance', 'is_active']
    search_fields = ['regno','fees', 'payment', 'balance', 'is_active']
    ordering_fields = ['regno','fees', 'payment', 'balance', 'is_active']

    queryset = FeesStructure.objects.filter(is_active=True).order_by('-id')
    
    
# detail view 
# retrieving one object 
class FeeDetailView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ] 

    queryset = FeesStructure.objects.all()

    serializer_class = FeesStructureSerializer
    
class UpdateFeesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeesStructure.objects.all()
    serializer_class = FeesStructureSerializer
    permission_classes = [permissions.AllowAny]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    
class AddFees(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny,
    ] 

    serializer_class = FeesStructureSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fees = serializer.save()

        return Response({
            "fee": FeesStructureSerializer(fees,
            context=self.get_serializer_context()).data, 
        })
    

# viewsets 
# from rest_framework import viewsets, permissions

# ModelViewset
# Create your views here.
# class FeesStructureViewSet(viewsets.ModelViewSet):
#     # queryset = Student.objects.all()
#     queryset = FeesStructure.objects.filter(is_active=True).order_by('-id')
#     serializer_class = FeesStructureSerializer
#     permission_classes = [ permissions.AllowAny ] 
#     pagination_class = CustomPageNumberPagination
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['regno','fees', 'payment', 'balance', 'is_active']
#     search_fields = ['regno','fees', 'payment', 'balance', 'is_active']
#     ordering_fields = ['regno','fees', 'payment', 'balance', 'is_active']
  

    # Single student fees
class StudentFeesView(generics.ListAPIView):
    permission_classes = [ permissions.AllowAny ]
    serializer_class = FeesStructureSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        student = self.kwargs['student']

        fees = FeesStructure.objects.filter(student=student, is_active=True).order_by('-id')

        if not fees:
            raise AuthenticationFailed('Student not found!')

        # Date Filters
        from_date = self.request.query_params.get('from_date',None)
        to_date = self.request.query_params.get('to_date',None)

        if from_date and to_date:
            date_format='%d-%m-%Y'
            from_date=datetime.strptime(from_date, date_format) #Convert string into date format
            to_date=datetime.strptime(to_date,date_format)
            to_date=to_date+timedelta(days=1) # add extra day in date search
            fees=fees.filter(payment_date__range=[from_date,to_date]) 

        return fees