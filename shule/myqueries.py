from shule.models import *

# get all students
students = Student.objects.all()

# get all teachers
teachers = Teacher.objects.all()

# get all parents
parents = Parent.objects.all()

#filter students by parent id
#get all students of parent 1
students = Parent.objects.get(id=1).student_set.all()
students = Student.objects.all().filter(id=1)

#get parent by student
stud1 = Student.objects.first()
parent_name = stud1.parent.parent_name

#filter students by class id
students = Student.objects.all().filter(class_level=1)

#filter assignments by class id
assignments =Assignment.objects.all().filter(assignment_class=1)




