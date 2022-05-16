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
            Member_Email = request.query_params["Member_Email"]
            if id != None:
                trans = transformation.objects.get(Member_Email=Member_Email)
                serializer = TransformationSerializer(trans)       
        except:
            trans1 = transformation.objects.all()
            serializer = TransformationSerializer(trans1, many = True)

        return Response(serializer.data)

    def post(self):
        pass