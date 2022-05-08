from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from programme.models import Chest, Back, Shoulders, Legs, Biceps, Triceps, Cardio, Programme 


from .serializers import  ChestSerializer, BackSerializer, ShouldersSerializer, LegsSerializer, BicepsSerializer, TricepsSerializer, CardioSerializer, ProgrammeSerializer 

class ChestList(APIView):
    
    def get(self, request):
        chest1 = Chest.objects.all()
        serializer = ChestSerializer(chest1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

class BackList(APIView):
    
    def get(self, request):
        back1 = Back.objects.all()
        serializer = BackSerializer(back1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

class ShouldersList(APIView):
    
    def get(self, request):
        shoulders1 = Shoulders.objects.all()
        serializer = ShouldersSerializer(shoulders1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

class LegsList(APIView):
    
    def get(self, request):
        legs1 = Legs.objects.all()
        serializer = LegsSerializer(legs1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

class BicepsList(APIView):
    
    def get(self, request):
        biceps1 = Biceps.objects.all()
        serializer = BicepsSerializer(biceps1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

class TricepsList(APIView):
    
    def get(self, request):
        triceps1 = Triceps.objects.all()
        serializer = TricepsSerializer(triceps1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

class CardioList(APIView):
    
    def get(self, request):
        cardio1 = Cardio.objects.all()
        serializer = CardioSerializer(cardio1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

class ProgrammeList(APIView):
    
    def get(self, request):
        programme1 = Programme.objects.all()
        serializer = ProgrammeSerializer(programme1, many = True)
        return Response(serializer.data)

    def post(self):
        pass