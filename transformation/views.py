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
    
    def get(self, request):

        try:
            queryset = transformation.objects.all()
            username = self.request.query_params.get('username')
            if username is not None:
                queryset = queryset.filter(Member_Email=username) 
            return queryset     
        except:
            trans1 = transformation.objects.all()
            serializer = TransformationSerializer(trans1, many = True)

        return Response(serializer.data)

    def post(self):
        pass