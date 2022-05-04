from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transformation.models import transformation

from .serializers import  TransformationSerializer


class TransformationList(APIView):
    
    def get(self, request):
        transformation1 = transformation.objects.all()
        serializer = TransformationSerializer(transformation1, many = True)
        return Response(serializer.data)

    def post(self):
        pass