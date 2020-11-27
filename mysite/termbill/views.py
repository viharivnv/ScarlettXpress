from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from myR.models import Course,Student
from pymongo import MongoClient

import math

@login_required
def bill(request):
    client = MongoClient("mongodb+srv://admin:segrp1scarletxpress@scarletcluster.mbgoy.mongodb.net/test")
    db = client.get_database('RUDB')
    students = db.myR_student
    username = request.user.username
    studentdata = students.find_one({'netID': username})
    Name=studentdata["FirstName"]+' ' + studentdata["LastName"]
    credits=studentdata["CreditsRegistered"]
    campusFee = 1144.95
    schoolFee = 104.75
    dbc = 119.99
    misc = 75.00
    CompFee = 171
    pirg = 11.2
    tution = credits * 915
    if credits>=4:
        tution =12*915
    fees=campusFee+schoolFee+tution+dbc+misc+CompFee+pirg
    paid=0.0
    balance="{:.2f}".format(fees-paid)
    fees="{:.2f}".format(fees)
    data = [
        {
            'Name': Name,
            'credits': str(credits),
            'ComputerFee': '$171.00',
            'PIRG': '$11.20',
            'CampusFee': '$845',
            'SchoolFee': '$104.75',
            'TutionFees': '$'+str(tution),
            'DigitalBookCharge': '$8629.89',
            'MISC': '$75.00',
            'TotalCharges': '$'+str(fees),
            'TotalPayments': '$'+str(paid),
            'BalanceDue': '$'+str(balance)

         }
    ]
    context={
        'data':data
    }
    return render(request, 'termbill/termbill.html', context)
