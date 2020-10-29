from django.shortcuts import render

def bill(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    return render(request, 'termbill/termbill.html')
