from .models import FeesStructure
from rest_framework import serializers

class FeesStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesStructure
        fields = ['id', 'regno','fees', 'payment', 'balance', 'is_active']