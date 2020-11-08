from pymongo import MongoClient
from django.shortcuts import render
from .models import Course, Student

def planner(request):
    return render(request, 'courseplanner.html')
