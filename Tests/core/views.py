from django.shortcuts import render

# Create your views here.
def testers(request):
    return render(request, 'core/testers.html')

def personality(request):
    return render(request, 'core/personality.html')

def aptitude(request):
    return render(request,'core/aptitude.html')

def choose(request):
    return render(request, 'core/choose.html')

def signin(request):
    return render(request, 'core/signin.html')

def createaccount(request):
    return render(request, 'core/createaccount.html')

def score(request):
    return render(request, 'core/score.html')

def assessments(request):
    return render(request, 'core/assessments.html')
