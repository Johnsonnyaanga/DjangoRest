
from rest_framework.views import APIView
from .models import Hero
from students.serializers import HeroSerializer
from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import status
# Create your views here.

class heroesList(APIView):
    def get(self,request):
        heroes1 = Hero.objects.all()
        serializer = HeroSerializer(heroes1,many=True)
        return Response(serializer.data)
        
    

