from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from member.models import Member

from .serializers import  MemberSerializer

class MemberList(APIView):
    
    def get(self, request):
        member1 = Member.objects.all()
        serializer = MemberSerializer(member1, many = True)
        return Response(serializer.data)

    def post(self):
        pass