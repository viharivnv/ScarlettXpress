from pymongo import MongoClient
from django.shortcuts import render
from .models import Course, Student

def planner(request):
    myclient = MongoClient('localhost', 27017)
    mydb = myclient["RUDB"]
    mycol = mydb["courseplanner_courses"]
    context = {}
    i = 1
    for doc in mycol.find():
        context["course"+i] = doc
        i += 1
    context["totalCourses"] = i

    return render(request, 'courseplanner.html', context)
