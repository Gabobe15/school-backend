from django.db import models
from django.utils import timezone

from mkuapi.models import Student

# Create your models here.
class FeesStructure(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    amount = models.CharField(max_length=255, null=True)
    payment_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    def _int_(self):
        return self.amount
    
 # fees = models.IntegerField(null=True)
    # payment = models.IntegerField(null=True)
    # balance = models.IntegerField(null=True)