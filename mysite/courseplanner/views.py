from pymongo import MongoClient
from django.shortcuts import render
import re
from .models import Course, Student

def planner(request):
    context = {}

    client = MongoClient("mongodb+srv://admin:segrp1scarletxpress@scarletcluster.mbgoy.mongodb.net/test")
    db = client.get_database('RUDB')
    courses = db.myR_course
    students = db.myR_student
    allCourses = courses.find()
    totalCourses = courses.find().count()
    context['totalCourses'] = totalCourses
    # i = 0
    # for course in allCourses:
    #     course['MeetingTimes'] = 'test'
    #     spaces = [m.start() for m in re.finditer(' ',course['MeetingTimes'])]
    #     for i in range(len(spaces)):
    #         if(i/4 > 0 and i%4 == 0):
    #             s = course['MeetingTimes']
    #             course['MeetingTimes'] = s[:i] + '<br>' + s[i+1:]

    context['allCourses'] = allCourses

    return render(request,'courseplanner.html',context)
