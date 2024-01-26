from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','regno', 'fullname', 'course', 'email', 'contact', 'is_active']
        
# Register Serializer

# class RegisterStudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('id', 'regno', 'fullname', 'course', 'email', 'contact', 'is_active')

#     def create(self, validated_data):
#         student = Student.objects.create_student(
#             validated_data['regno'],
#             validated_data['fullname'],
#             validated_data['course'],
#             validated_data['email'],
#             validated_data['contact'],
#             validated_data['is_active'],
#         )

#         return student