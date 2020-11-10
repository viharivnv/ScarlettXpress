from django.db import models

class Course(models.Model):
    FullCode = models.CharField(max_length=10, default=None)
    Index = models.IntegerField(default=None)
    Title = models.CharField(max_length=500, blank=True, null=True)
    Instructors = models.CharField(max_length=500)
    Credits = models.IntegerField(default=None)
    MeetingType = models.CharField(max_length=100, blank=True, null=True)
    Status = models.BooleanField(default=True)
    Enrolled = models.IntegerField(blank=True, null=True)
    Capacity = models.IntegerField(blank=True, null=True)
    MeetingTimes = models.CharField(max_length=100)



class Student(models.Model):
    netid = models.CharField(max_length=10, default=None)
    RUID = models.IntegerField(blank=True, null=True)
  # Password = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=50,blank=True, null=True)
    LastName = models.CharField(max_length=50,blank=True, null=True)
    DegreeLevel = models.CharField(max_length=50,blank=True, null=True)
    CreditsRegistered = models.IntegerField(blank=True, null=True)
    CreditsTaken = models.IntegerField(blank=True, null=True)
    CoursesRegistered = models.IntegerField(blank=True, null=True)
    CoursesTaken =  models.IntegerField(blank=True, null=True)

