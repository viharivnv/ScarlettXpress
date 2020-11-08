import pymongo
from django.shortcuts import render
from .models import Course, Student

coursesList = []
newSchedule = []

def planner(request):
    myclient = pymongo.mongo_client("mongodb://localhost:27017/")
    mydb = myclient["RUDB"]
    mycol = mydb["courseplanner_courses"]
    context = {}
    i = 1
    for doc in mycol.find():
        context["course"+i] = doc

    return render(request, 'courseplanner/courseplanner.html')
