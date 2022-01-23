
from rest_framework.views import APIView
from shule.models import *
from shule.Serializers import StudentSerializer
from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import status
# Create your views here.

class StudentList(APIView):
    def get(self, request):
        # students = Student.objects.all()
        # serializer = StudentSerializer(students,many=True)
        data = list(Student.objects.all().values())
        return Response(data)
