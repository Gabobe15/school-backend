from .models import FeesStructure
from rest_framework import serializers

class FeesStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesStructure
        fields = ['id','student', 'payment_date', 'amount']