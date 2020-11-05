from django.db import models

from django.contrib.auth.models import User

class Course(models.Model):
    Index=models.IntegerField()
    FullCode = models.CharField(max_length=10, primary_key=True)
    Instructors = models.CharField(max_length=500)
    Status = models.CharField(max_length=10)
    MeetingTimes = models.CharField(max_length=100)
    Capacity=models.IntegerField()
    Enrolled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course'

class Student(models.Model):
    Student = models.CharField(max_length=50)
    netId = models.IntegerField()
    ruId = models.IntegerField()
    credits = models.IntegerField()
    gradelevel =  models.CharField(max_length=50)
    CoursesTaken =  models.CharField(max_length=1000)
    class Meta:
        managed = False
        db_table = 'students'