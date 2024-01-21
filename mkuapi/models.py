from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    regno = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100, blank=True)
    course = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, unique=True, blank=True)
    contact = models.CharField(max_length=100, default=1, blank=True)
    is_active = models.BooleanField(default=True)
    date_reg = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.regno
    
    
    
    
 