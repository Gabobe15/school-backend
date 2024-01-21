from django.urls import path
from . import views

urlpatterns = [ 
    path('forgot-password/', views.ForgotPasswordAPIView.as_view(), name="forgot-password"),
    path('verify-token/<slug:token>/', views.VerifyTokenAPIView.as_view(), name="verify-token"),
    path('reset-password/', views.ResetPasswordAPIView.as_view(), name="reset-password"),
    path('users/', views.UserListView.as_view(), name="auth-users-list"),
    path('inactive/', views.InactiveListView.as_view(), name="inactive-users-list"),
    path('update-user/<int:pk>/', views.UpdateUserView.as_view(), name="update-user"),
    path('register/', views.RegisterUser.as_view(), name="auth-register"),
    path('login/', views.LoginView.as_view(), name="auth-login"),
    path('user/', views.UserAPI.as_view(), name="auth-user"),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logoutall/', views.LogoutAllView.as_view(), name='logoutall')
    # path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset'))
]



    # from knox import views as knox_views
    # path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall')
