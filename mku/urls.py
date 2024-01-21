from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mkuapi/', include('mkuapi.urls')),
    path('fees_structure/', include('fees_structure.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
