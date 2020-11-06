from django.shortcuts import render

def planner(request):
    return render(request, 'courseplanner/courseplanner.html')
