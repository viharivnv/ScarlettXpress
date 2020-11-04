from django.shortcuts import render

def bill(request):
    return render(request, 'termbill/termbill.html')
