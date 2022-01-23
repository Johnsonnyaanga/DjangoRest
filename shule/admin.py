from django.contrib import admin
from .models import Parent
from .models import Student
from .models import Assignment
from .models import AssignmentStatus
from .models import Teacher
from .models import ClassLevel



# Register your models here.
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(Assignment)
admin.site.register(AssignmentStatus)
admin.site.register(ClassLevel)