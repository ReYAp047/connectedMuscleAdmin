from rest_framework import serializers
from .models import transformation 

class TransformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = transformation
        fields = '__all__'