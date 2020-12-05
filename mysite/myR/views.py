from django.shortcuts import render

from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from myR.models import Course,Student
from pymongo import MongoClient

@login_required
def home(request):
    client = MongoClient("mongodb+srv://admin:segrp1scarletxpress@scarletcluster.mbgoy.mongodb.net/test")
    db = client.get_database('RUDB')
    students = db.myR_student
    username = request.user.username
    studentdata = students.find_one({'netID': username})
    Name = studentdata["FirstName"] + ' ' + studentdata["LastName"]
    credits = studentdata["CreditsRegistered"]
    duedate = studentdata["DueDate"]
    duedate = duedate.date()
    data = [
        {
            'DueDate': str(duedate),
            'Name': Name,
            'NetID': username,
            'credits': str(credits),


        }
    ]
    context = {
        'data': data
    }
    return render(request, 'myR/home.html',context)
