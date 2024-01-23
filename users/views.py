from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, permissions, generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token


from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, ChangePasswordSerializer
from knox.models import AuthToken

# forget password 
from django.conf import settings
from django.core.mail import send_mail
from .models import PasswordReset


import random, string, datetime


from rest_framework.views import APIView 

import pytz


from rest_framework import status


User = get_user_model()
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class UserListView(generics.ListAPIView):
    permission_classes = [ permissions.AllowAny, ] 
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name', 'last_name', 'role', 'location', 'mobile', 'email']
    search_fields = ['first_name', 'last_name', 'role', 'location', 'mobile', 'email']
    ordering_fields = ['first_name', 'last_name', 'role', 'location', 'mobile', 'email']
    queryset = User.objects.filter(is_active=True, is_superuser=False).order_by('-id')
    
# Detail view -- single user view
class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ] 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class InactiveListView(generics.ListAPIView):
    permission_classes = [ permissions.AllowAny, ] 
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name', 'last_name', 'role', 'location', 'mobile', 'email']
    search_fields = ['first_name', 'last_name', 'role', 'location', 'mobile', 'email']
    ordering_fields = ['first_name', 'last_name', 'role', 'location', 'mobile', 'email']
    queryset = User.objects.filter(is_active=False, is_superuser=False).order_by('-id')
    
# Regster user view

class RegisterUser(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny,
    ] 

    serializer_class = RegisterSerializer
           
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = request.data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            # raise serializers.ValidationError("This email already exists!.")
            # raise ValidationError('Email already exists!')
            raise AuthenticationFailed('Email already exists!')
        else:
            user = serializer.save()

            return Response({
                "user": UserSerializer(user,
                context=self.get_serializer_context()).data, 
                "token": AuthToken.objects.create(user)[1]
            })
# Login user view
class LoginView(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
 
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data, 
            "token": AuthToken.objects.create(user)[1]
        })
        
#  Get current loggedin user

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ] 

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user 

# Update user
class UpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny,]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


# Forgot password
class ForgotPasswordAPIView(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def post(self, request):
        email = request.data['email']
        token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))

        PasswordReset.objects.create(email=email, token=token)

        send_mail(
            subject = 'Reset your password!',
            message='Click <a href="http://localhost:3000/reset-password/' + token + '">here</a> to reset your password!',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [email]
        )

        return Response ({
            'message': 'Please check your email!'
        })
        

# Verify token
class VerifyTokenAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def retrieve(self, request, *args, **kwargs):
        token = kwargs['token']

        tokenObj = PasswordReset.objects.filter(token=token).first()

        if not tokenObj:
            raise AuthenticationFailed('Token not found!')

        if tokenObj.status == 'used':
            raise AuthenticationFailed('Token used!')

        utc_now = datetime.datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        if tokenObj.date_created < utc_now - datetime.timedelta(hours=1):
            raise AuthenticationFailed('Token has expired!')

        return Response({
            'message': 'Token is valid!'
        })
        

# Reset password
class ResetPasswordAPIView(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def post(self, request):
        data = request.data

        passwordReset = PasswordReset.objects.filter(token=data['token']).first()

        user = User.objects.filter(email=passwordReset.email).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        user.set_password(data['password'])
        user.save()

        passwordReset.status = 'used'
        passwordReset.save()

        return Response({
            'message': 'Password changed successfully.'
        })
        
        
# Change password
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User

    permission_classes = [
        permissions.AllowAny,
    ]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("currentPassword")):
                return Response({"currentPassword": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

# set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("newPassword"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Delete the user's token to logout
            request.auth.delete()  # Assuming the token is stored in `request.auth`
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LogoutAllView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Delete all tokens associated with the user
            Token.objects.filter(user=request.user).delete()
            return Response({'message': 'Successfully logged out from all devices.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)