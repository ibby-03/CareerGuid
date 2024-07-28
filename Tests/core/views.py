from django.shortcuts import render
from .forms import SignupForm

# Create your views here.
def testers(request):
    return render(request, 'core/testers.html')

def personality(request):
    return render(request, 'core/personality.html')

def aptitude(request):
    return render(request,'core/aptitude.html')

def signin(request):
    context ={}
    return render(request, 'core/signin.html', context)

def createaccount(request):
    context = {}
    return render(request, 'core/createaccount.html', context)
    # if request.method == 'POST':
    #     form = SignupForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
            
    #         return redirect('/login/')
    # else:  
    #     form = SignupForm()
        
    # return render(request, 'core/createaccount.html', {'form':form})

def score(request):
    return render(request, 'core/score.html')

def assessments(request):
    return render(request, 'core/assessments.html')

def homepage(request):
    return render(request, 'core/homepage.html')

def roadmappage(request):
    return render(request, 'core/roadmappage.html')

def currenttrends(request):
    return render(request, 'core/currenttrends.html')
