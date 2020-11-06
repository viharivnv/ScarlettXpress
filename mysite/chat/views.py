from django.shortcuts import render

def chat(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    return render(request, 'chat/chat.html')
