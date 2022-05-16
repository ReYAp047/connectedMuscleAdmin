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

            transformations = transformation.objects.filter(Member_Email=Member_Email)
            serializer = TransformationSerializer(transformations, many = True)

            return Response(serializer.data)   

        def post(self, request, *args, **kwargs):
            transformation_data = request.data

            new_trans = transformation.objects.create(Member_Email=transformation_data["Member_Email"], Week_Date=transformation_data[
                "Week_Date"], Week_Goal=transformation_data["Week_Goal"], Body_Height=transformation_data["Body_Height"], Body_Weight=transformation_data["Body_Weight"]
                , Image_Link=transformation_data["Image_Link"])

            new_trans.save()

            serializer = TransformationSerializer(new_trans)

            return Response(serializer.data)