from django.shortcuts import render
from datetime import datetime
from pymongo import MongoClient
from django.contrib.auth.decorators import login_required

context = {
    "currchatid": 0,
    "chats": {},
    "conversations": []
}


@login_required
def chat(request):
    global context
    client = MongoClient("mongodb+srv://admin:segrp1scarletxpress@scarletcluster.mbgoy.mongodb.net/test")
    db = client.get_database('RUDB')
    conversations = db.chat_conversation
    chats = db.chat_message
    students = db.myR_student

    username = request.user.username
    context['conversations'] = conversations.find_one({'netID': username})["chats"]
    context['currchatid'] = context["conversations"][0]
    for c in context["conversations"]:
        context["chats"][c] = chats.find_one({"id": c}, {"_id": 0})

    if request.method == 'POST':
        for key, y in request.POST.items():
            if key == "csrfmiddlewaretoken":
                continue

            elif key[0:6] == "search":
                search = key[7:]
                results = []
                for c in context["conversations"]:
                    for m in chats.find_one({'id': c}).members:
                        if search.lower() in m.lower():
                            results.append(c)
                            break
                context["conversations"] = results

            elif key[0:6] == "switch":
                chatid = key[7:]
                print(chatid)
                if id in context["conversations"]:
                    context['currchatid'] = int(chatid)

            elif key[0:4] == "send":
                message = key[5:]
                print(message)
                m = {"sender": username, "message": message, "time": datetime.now()}
                chats.update_one({"messages": chats.find_one({"id": context["currchatid"]})["messages"]},
                                 {"$set": {"messages": chats.find_one({
                                     "id": context["currchatid"]})["messages"].append(m)}})

            elif key[0:3] == "add":
                users = key[4:]
                users = users.split(" ")
                print(users)
                temp = []
                for u in users:
                    for i in students.find({"username": u}):
                        temp.append(u)
                users = temp
                index = chats.count()
                chats.insert_one({"messages": [], "id": index, "members": users.append(username)})
                conversations.update_one({"netID": username},
                                         {"$set": {"chats": conversations.find_one({"netId": username})["chats"].append(index)}})
                for u in users:
                    conversations.update_one({"netID": u},
                                             {"$set": {"chats": conversations.find_one({"netId": u})["chats"].append(index)}})
    return render(request, 'chat/chat.html', context)
