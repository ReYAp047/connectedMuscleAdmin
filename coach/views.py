from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from coach.models import Coach

from .serializers import  CoachSerializer

class CoachList(APIView):
    
    def get(self, request):
        coach1 = Coach.objects.all()
        serializer = CoachSerializer(coach1, many = True)
        return Response(serializer.data)

    def post(self):
        pass