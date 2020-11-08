# from django.db import models
from djongo import models
from django.contrib.auth.models import User

class Course(models.Model):
    FullCode = models.CharField(max_length=10, primary_key=True)
    Index=models.IntegerField(max_length=5)
    Title = models.CharField(max_length=500,blank=True, null=True)
    Instructors = models.CharField(max_length=500)
    courseCredits = models.IntegerField(blank=True, null=True)
    MeetingType = models.CharField(max_length=100,blank=True, null=True)
    Status = models.BooleanField(default=True)
    Enrolled = models.IntegerField(blank=True, null=True)
    Capacity = models.IntegerField(blank=True, null=True)
    MeetingTimes = models.CharField(max_length=100)
    def __str__(self):
        return self.Title


class Student(models.Model):
    netid = models.IntegerField(max_length=6,blank=True, null=True)
    RUID = models.IntegerField(max_length=50,blank=True, null=True)
  # Password = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=50,blank=True, null=True)
    LastName = models.CharField(max_length=50,blank=True, null=True)
    DegreeLevel = models.CharField(max_length=50,blank=True, null=True)
    CreditsRegistered = models.IntegerField(max_length=15,blank=True, null=True)
    CreditsTaken = models.IntegerField(max_length=15,blank=True, null=True)
    CoursesRegistered = models.IntegerField(max_length=15,blank=True, null=True)
    CoursesTaken =  models.IntegerField(max_length=15,blank=True, null=True)
    def __str__(self):
        return self.FirstName + " " + self.LastName

