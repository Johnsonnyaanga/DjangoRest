from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

        
class Parent(models.Model):
    parent_name = models.CharField(max_length=250,null= True)
    phoneNumber = models.CharField(max_length=250,null= True)
    email =  models.EmailField(null= True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.parent_name
    
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=250,null= True)
    phoneNumber = models.CharField(max_length=250,null= True)
    profile_image = models.CharField(max_length=250,null= True)
    email =  models.EmailField(null= True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.teacher_name   

class ClassLevel(models.Model):
    class_name = models.CharField(max_length=250,null= True)
    class_teacher = models.ForeignKey(Teacher,null= True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.parent_name
       
        
class Student(models.Model):
    Stud_name = models.CharField(max_length=250,null= True)
    profile_image = models.CharField(max_length=250,null= True)
    admssion_number =  models.IntegerField(null= True)
    parent = models.ForeignKey(Parent,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.Stud_name
    
class Assignment(models.Model):
    title = models.CharField(max_length=250,null= True)
    strand = models.CharField(max_length=250,null= True)
    sub_strand = models.CharField(max_length=250,null= True)
    description = models.CharField(max_length=250,null= True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    due_date = models.DateField(null=True)
    teacher = models.ForeignKey(Teacher,null=True,on_delete=models.SET_NULL)
    assignment_class = models.ForeignKey(ClassLevel,null=True,on_delete=models.SET_NULL)
    student = models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
    
class AssignmentStatus(models.Model):
    STATUS_CHOICE = (
        ('completed','complete'),
        ('incompleted','incomplete'),
    )
    assignment = models.ForeignKey(Assignment,null=True,on_delete=models.SET_NULL)
    student = models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)
    status = models.CharField(max_length=250,null=True,choices=STATUS_CHOICE)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.stat  
    