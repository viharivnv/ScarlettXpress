from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from pymongo import MongoClient
from django.contrib.auth.decorators import login_required

context = {
    "username": "",
    "currchatid": -1,
    "chats": {},
    "conversations": [],
    "help": 0,
    "helpchat": []
}

@login_required
def chat(request):
    return render(request, "chat/chat.html")

@login_required
def getcontext(request):
    global context
    client = MongoClient("mongodb+srv://admin:segrp1scarletxpress@scarletcluster.mbgoy.mongodb.net/test")
    db = client.get_database("RUDB")
    conversations = db.chat_conversation
    chats = db.chat_message
    students = db.myR_student

    username = request.user.username
    context["username"] = username
    context["conversations"] = conversations.find_one({"netID": username})["chats"]
    if context["currchatid"] == -1 and len(context['conversations'])>0:
        context["currchatid"] = context["conversations"][0]
    for c in context["conversations"]:
        context["chats"][c] = chats.find_one({"id": c}, {"_id": 0})

    if request.method == "POST":
        for key, y in request.POST.items():
            if key == "csrfmiddlewaretoken":
                continue

            elif key == "switch":
                chatid = int(y)
                if chatid in context["conversations"]:
                    context["currchatid"] = int(chatid)
                    context["help"] = 0

            elif key == "help":
                context["help"] = 1

            elif key == "send":
                message = y
                if message:
                    m = {"sender": username, "message": message}
                    if context["help"] > 0:
                        helprequests = db.chat_help.find_one()
                        context["helpchat"].append(m)
                        for r in helprequests:
                            if r in message:
                                context["helpchat"].append({"sender": "helpbot", "message": helprequests[r]})
                    else:
                        c = chats.find_one({"id": context["currchatid"]})["messages"]
                        c.append(m)
                        chats.update_one({"id": context["currchatid"]},
                                         {"$set": {"messages": c}})

            elif key == "add":
                users = y
                users = users.split(" ")
                temp = []
                for u in users:
                    for i in students.find({"netID": u}):
                        temp.append(u)
                users = temp
                if len(users) > 0:
                    index = chats.count()
                    users.append(username)
                    chats.insert_one({"messages": [], "id": index, "members": users})
                    for u in users:
                        c = conversations.find_one({"netID": u})["chats"]
                        c.append(index)
                        conversations.update_one({"netID": u}, {"$set": {"chats": c}})
    return JsonResponse(context, safe=True)
