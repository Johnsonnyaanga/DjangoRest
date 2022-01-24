
from rest_framework.views import APIView

from shule.serializers import StudentSerializer
from shule.models import Student
from rest_framework.response import Response


class StudentList(APIView):
    def get(self,request):
        heroes1 = Student.objects.all()
        serializer = StudentSerializer(heroes1,many=True)
        return Response(serializer.data)
