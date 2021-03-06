from django.shortcuts import render
from datetime import timedelta, datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

#THE VALUES IN CART, REGISTERED, AND CREDITS WILL BE DISPLAYED ON THE PAGE
context = {
    "cart": {},
    "registered":{},
    "numincart": 0,
    "numregistered": 0,
    "credits": 0,
    "coursestaken" : 0,
    "needspn": []
}

# netid : ss3020
#print(list(students.find()))

def index(request):
    global context

    #CONNECT TO THE DATABASE MANUALLY
    client = MongoClient("mongodb+srv://admin:segrp1scarletxpress@scarletcluster.mbgoy.mongodb.net/test")
    db = client.get_database('RUDB')
    courses = db.myR_course
    students = db.myR_student


    #Put the signed in users info in student data
    #studentdata = students.find_one({'netID': 'ss3020'})

    studentdata = students.find_one({'netID': 'nvv13'})
    print(studentdata)




    context["coursestaken"] = studentdata["CoursesTaken"]
    #Fill the Registered section on the website with the already registered classes from the database
    context["credits"] = studentdata["CreditsRegistered"]
    alreadyregistered = studentdata['CoursesRegistered']
    takenclasses = studentdata["CoursesTaken"]
    print(alreadyregistered)
    for i in alreadyregistered:
        print(i)
        temp = courses.find_one({'_id': ObjectId(i)})
        context["registered"].update({i:[temp['Title'], temp['MeetingTimes'], temp['Credits']]})


    #Get the list of all the available courses
    context["data"] = list(courses.find())[100:200]

    #Create a list of classes that the user can't register for due to Prereqs issue. Save in context["needspn]
    for i in range(0,len(context["data"])):
        if len(context["data"][i]["Prerequisites"])>20 and len(context["data"][i]["Prerequisites"])<33:
            x,y = context["data"][i]["Prerequisites"].split("OR")
            x = x.replace('(','')
            x = x.replace(")","")
            x = x.replace(":","")
            y = y.replace('(','')
            y = y.replace(")","")
            y = y.replace(":","")
            if x in takenclasses or y in takenclasses:
                print()
            else:
                context['needspn'].append(context["data"][i]["_id"])
        elif len(context["data"][i]["Prerequisites"])>5 and len(context["data"][i]["Prerequisites"])<13:
            x = x.replace('(','')
            x = x.replace(")","")
            x = x.replace(":","")
            if x in takenclasses:
                print()
            else:
                context['needspn'].append(context["data"][i]["_id"])
    print(context["needspn"])



    if request.method == 'POST':
        #EVERY TIME A USER CLICKS ONY BUTTON
        for key,y in request.POST.items():
            if key == "csrfmiddlewaretoken":
                continue

            #If the User wishes to add a class to the cart
            elif key[0:4] == "Cart":
                #Get the id of the class, get more info of class from the id and store in context['cart']
                wd,ids = key.split('-')
                temp = courses.find_one({'_id': ObjectId(ids)})
                print(ids)
                context['cart'].update({ids:[ temp['Title'],temp['MeetingTimes'], temp['Credits']]})

            #If THE USER WISHES TO REGISTER CLASSES FROM THE CART
            elif key == "registerclass":
                if (context["credits"]<19 ):  #FIX YHIS FIX THIS FIX THIS FIX THIS
                    idsofclasstaken = []
                    #BASICALLY STORE THE CART ARRAY IN THE DATABASE
                    #loop for the number of claases in the cart
                    for i in list(context["cart"]):
                        context['temp'] = context["cart"][i]
                        context["registered"].update({i: context["temp"]})
                        context["credits"] = context["credits"] + int(context["temp"][2])
                        temp = courses.find_one({'_id': ObjectId(i)})

                        #INCREASE THE NUMBER OF CLASSES TAKEN BY THE USER
                        #context["coursestaken"] = context["coursestaken"] + 1

                        #INCREASE THE NUMBER OF SEATS IN CLASS BY 1
                        newseats = temp['Enrolled'] + 1
                        #newseats = { 'Enrolled' : newseats , 'CoursesTaken' : context["coursestaken"]}
                        newseats = {'Enrolled': newseats}
                        courses.update_one({'_id' : ObjectId(i)}, {'$set': newseats} )
                        #UPDATE THE PAGE TO UPDATE THE SEATS NUMBER
                        context["data"] = list(courses.find())[100:200]

                        #creditss = { "CreditsRegistered" : context["credits"] , "CoursesTaken": context["coursestaken"]}
                        creditss = {"CreditsRegistered": context["credits"]}
                        idsofclasstaken.append(i)
                        #AFTER REGISTERING, DELETE THE CLASS FROM THE CART
                        del context["cart"][i]

                    taken = {"CoursesRegistered": idsofclasstaken}
                    duedate = datetime.today() + timedelta(days = 14)
                    print(duedate)
                    dd = { "DueDate": duedate}
                    students.update_one({'netID': 'nvv13'} , {'$set': dd} )

                    #UPDATE THE DATABASE FOR THE CREDITS AND CLASSES REGISTERD COLUMNS
                    students.update_one({'netID': 'nvv13'} , {'$set': creditss} )
                    students.update_one({'netID': 'nvv13'}, {'$set': taken})

            #WHEN THE USER WISHES TO DROP A COURSE
            elif key[0:4] == "Drop":
                wd, ids = key.split('-')
                #FIND THE REGISTERED CLASSES FOR THE USER FROM THE DATABASE
                temp = courses.find_one({'_id': ObjectId(ids)})
                deleteclass = studentdata['CoursesRegistered']
                for i in deleteclass:
                    if(str(temp["_id"])==i):
                        deleteclass.remove(i)
                #DELETE THE DROPPED CLASS AND STORE IT BACK IN THE DATABASE - ALSO UPDATE THE CREDITS
                context['credits'] = context['credits'] - temp['Credits']
                deleteclass = { "CreditsRegistered" : context["credits"] , 'CoursesRegistered' : deleteclass }
                del context['registered'][ids]
                students.update_one({'netID': 'nvv13'}, {'$set': deleteclass})

                # REDUCE THE NUMBER OF CLASSES TAKEN BY THE USER
                #context["coursestaken"] = context["coursestaken"] - 1

                # DECREASE THE NUMBER OF SEATS IN CLASS BY 1
                newseats = temp['Enrolled'] - 1
                # newseats = { 'Enrolled' : newseats , 'CoursesTaken' : context["coursestaken"]}
                newseats = {'Enrolled': newseats}
                courses.update_one({'_id': ObjectId(i)}, {'$set': newseats})
                # UPDATE THE PAGE TO UPDATE THE SEATS NUMBER
                context["data"] = list(courses.find())[100:200]
                #creditss = {"CoursesTaken": context["coursestaken"]}

            elif key[0:3] == "Spn":
                print()






    # return response
    return render(request,'webreg/regpage.html',context)