from rest_framework import serializers

from shule.models import *

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('Stud_name','profile_image', 'admssion_number','parent','date_created','class_level')