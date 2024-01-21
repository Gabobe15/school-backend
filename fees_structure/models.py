from django.db import models
from django.utils import timezone

from mkuapi.models import Student

# Create your models here.
class FeesStructure(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    regno = models.CharField(max_length=255, null=True)
    fees = models.CharField(max_length=255, null=True)
    payment = models.CharField(max_length=255, null=True)
    balance = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    date_reg = models.DateTimeField(default=timezone.now)
    
    def _int_(self):
        return self.regno
    
 # fees = models.IntegerField(null=True)
    # payment = models.IntegerField(null=True)
    # balance = models.IntegerField(null=True)