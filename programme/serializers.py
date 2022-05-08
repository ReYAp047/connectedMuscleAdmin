from rest_framework import serializers
from .models import Chest, Back, Shoulders, Legs, Biceps, Triceps, Cardio, Programme 

class ChestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chest
        fields = '__all__'

class BackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Back
        fields = '__all__'

class ShouldersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoulders
        fields = '__all__'

class LegsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legs
        fields = '__all__'

class BicepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biceps
        fields = '__all__'

class TricepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triceps
        fields = '__all__'

class CardioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardio
        fields = '__all__'

class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = '__all__'