from django.http import HttpResponse
from django.template import loader
from .models import Conversation

def chat(request):
    if not request.user.is_authenticated:
        return loader.render(request, 'users/login.html')
    return loader.render(request, 'chat/chat.html')
