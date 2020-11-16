from djongo import models

class Course(models.Model):
    courseID = models.IntegerField()
    sectionNumber = models.CharField(max_length=3)
    Index = models.IntegerField(primary_key=True)
    Instructors = models.TextField()
    Title = models.TextField()
    Credits = models.IntegerField()
    MeetingType = models.CharField(max_length=20)
    Status = models.BooleanField()
    Enrolled = models.IntegerField()
    Capacity = models.IntegerField()
    MeetingTimes = models.TextField()
    def __str__(self):
        return self.Title


class Student(models.Model):
    netID = models.TextField(primary_key=True)
    RUID = models.IntegerField()
  # Password = models.CharField(max_length=20)
    FirstName = models.TextField()
    LastName = models.TextField()
    DegreeLevel = models.CharField(max_length=2)
    CreditsRegistered = models.IntegerField()
    CreditsTaken = models.IntegerField()
    CoursesRegistered = models.IntegerField()
    CoursesTaken =  models.IntegerField()
    def __str__(self):
        return self.FirstName + " " + self.LastName
