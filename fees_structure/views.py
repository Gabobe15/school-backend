from django.shortcuts import render
from .models import FeesStructure
from .serializers import FeesStructureSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
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
  

    