from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transformation.models import transformation

from .serializers import  TransformationSerializer

#12
class TransformationList(APIView):
        serializer_class  = TransformationSerializer

        def get_queryset(self):
            Transformations = transformation.objects.all()
            return Transformations
        
        def get(self, request):
            Member_Email = request.query_params["Member_Email"]
            print(Member_Email)

            transformations = self.get_queryset()
            serializer = TransformationSerializer(transformations, many = True)

            return Response(serializer.data)   

    def post(self):
        pass