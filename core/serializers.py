from rest_framework import serializers
from .models import EmailRecord  # Ensure this model exists

class EmailRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailRecord
        fields = '__all__'  # Include all fields, or specify the ones you need
