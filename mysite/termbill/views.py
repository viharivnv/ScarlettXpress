from django.shortcuts import render

def bill(request):
    credits = 1
    credits *= 3950

    data = [
        {'credits': str(credits)
         }
    ]
    context={
        'data':data
    }
    return render(request, 'termbill/termbill.html', context)
