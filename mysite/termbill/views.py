from django.shortcuts import render
from myR.models import *
def bill(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    username=request.user.username
    record = Student.objects.filter(netId=username)
    credits=record.credits
    credits*=3950
    data={'credits':credits}
    return render(request, 'termbill/termbill.html',data)
