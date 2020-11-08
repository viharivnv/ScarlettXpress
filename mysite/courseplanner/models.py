from django.db import models

# Create your models here.

class Course(models.Model):
    Title = models.CharField(max_length=200, default='COURSE_NAME')
    FullCode = models.CharField(max_length=10, primary_key=True)
    Instructors = models.CharField(max_length=500)
    Status = models.CharField(max_length=10)
    MeetingTimes = models.CharField(max_length=100)
    Capacity = models.IntegerField()
    Enrolled = models.IntegerField()
    Semester = models.CharField(max_length=6)

    class Meta:
        managed = True
        db_table = 'courseplanner_course'

class Student(models.Model):
    Student = models.CharField(max_length=50)
    netId = models.IntegerField()
    ruId = models.IntegerField()
    credits = models.IntegerField()
    gradelevel =  models.CharField(max_length=50)
    CoursesTaken =  models.CharField(max_length=1000)
    class Meta:
        managed = True
        db_table = 'courseplanner_students'