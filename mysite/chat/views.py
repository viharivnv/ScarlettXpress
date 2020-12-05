from django.shortcuts import render
from datetime import datetime
from pymongo import MongoClient
from django.contrib.auth.decorators import login_required

context = {
    "currchatid": 0,
    "currentchat": {},
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

    chatlist = conversations.find_one({'netID': username})
    chatlist = chatlist['chats']
    context['conversations'] = chatlist

    if request.method == 'POST':
        for key, y in request.POST.items():
            if key == "csrfmiddlewaretoken":
                continue

            elif key[0:6] == "update":
                search = key[7:]
                print(search)
                results = []
                for c in context["conversations"]:
                    for m in chats.find_one({'id': c}).members:
                        if search.lower() in m.lower():
                            results.append(c)
                            break
                context["conversations"] = results
                context["currchat"] = chats.find_one({"id": context["currchatid"]})

            elif key[0:6] == "switch":
                chatid = key[7:]
                print(chatid)
                if id in chatlist:
                    context['currchatid'] = int(chatid)
                    context['currchat'] = chats.find_one({'id': int(chatid)})

            elif key[0:4] == "send":
                message = key[5:]
                print(message)
                m = {"sender": username, "message": message, "time": datetime.now()}
                chats.update_one({"messages": chats.find_one({"id": context["currchatid"]})["messages"]},
                                 {"$set": {"messages": chats.find_one({
                                     "id": context["currchatid"]})["messages"].append(m)}})
                context['currchat'] = chats.find_one({"id": context["currchatid"]})

            elif key[0:3] == "add":
                users = key[4:]
                users = users.split(" ")
                print(users)
                for u in users:
                    temp = []
                    for i in users.find({"username": u}):
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
