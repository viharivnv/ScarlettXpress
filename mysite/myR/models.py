# from django.db import models
from djongo import models
from django.contrib.auth.models import User

class Course(models.Model):
    FullCode = models.CharField(max_length=10, primary_key=True)
    Index = models.IntegerField()
    Title = models.CharField(max_length=500, blank=True, null=True)
    Instructors = models.CharField(max_length=500)
    Credits = models.IntegerField(default=0)
    MeetingType = models.CharField(max_length=100, blank=True, null=True)
    Status = models.BooleanField(default=True)
    Enrolled = models.IntegerField(blank=True, null=True)
    Capacity = models.IntegerField(blank=True, null=True)
    MeetingTimes = models.CharField(max_length=100)
    def __str__(self):
        return self.Title


class Student(models.Model):
    netid = models.IntegerField(blank=True, null=True)
    RUID = models.IntegerField(blank=True, null=True)
  # Password = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=50,blank=True, null=True)
    LastName = models.CharField(max_length=50,blank=True, null=True)
    DegreeLevel = models.CharField(max_length=50,blank=True, null=True)
    CreditsRegistered = models.IntegerField(blank=True, null=True)
    CreditsTaken = models.IntegerField(blank=True, null=True)
    CoursesRegistered = models.IntegerField(blank=True, null=True)
    CoursesTaken =  models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.FirstName + " " + self.LastName

