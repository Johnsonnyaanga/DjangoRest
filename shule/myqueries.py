from shule.models import *

# get all students
students = Student.objects.all()

# get all teachers
teachers = Teacher.objects.all()

# get all parents
parents = Parent.objects.all()

#filter students by parent id
students = Student.objects.all().filter(id=1)

#filter students by class id
students = Student.objects.all().filter(class_level=1)

#filter assignments by class id
assignments =Assignment.objects.all().filter(assignment_class=1)


