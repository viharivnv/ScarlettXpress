# from django.db import models
from djongo import models
from django.contrib.auth.models import User

class Course(models.Model):
    FullCode = models.CharField(max_length=10, primary_key=True)
    Index=models.IntegerField(max_length=5)
    Title = models.CharField(max_length=500)
    Instructors = models.CharField(max_length=500)
    Credits = models.IntegerField(max_length=3)
    MeetingType = models.CharField(max_length=100)
    Status = models.BooleanField(default=True)
    Enrolled = models.IntegerField(max_length=5)
    Capacity = models.IntegerField(max_length=5)
    MeetingTimes = models.CharField(max_length=100)
    def __str__(self):
        return self.Title


class Student(models.Model):
    Student = models.CharField(max_length=50)
    netid = models.IntegerField(max_length=6)
    RUID = models.IntegerField(max_length=50)
  # Password = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    DegreeLevel = models.CharField(max_length=50)
    CreditsRegistered = models.IntegerField(max_length=15)
    CreditsTaken = models.IntegerField(max_length=15)
    CoursesRegistered = models.IntegerField(max_length=15)
    CoursesTaken =  models.IntegerField(max_length=15)
    def __str__(self):
        return self.FirstName + " " + self.LastName

