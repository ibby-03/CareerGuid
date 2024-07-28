from django.shortcuts import render
from .forms import SignupForm
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Result
from .forms import SignupForm, AptitudeForm
from .models import AptitudeQuestion, AptitudeAnswer
from django.contrib.auth.models import User



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

@login_required
def take_quiz(request):
    if request.method == "POST":
        user = request.user  # Ensuring that only logged-in users can submit answers
        for key, value in request.POST.items():
            if key.startswith("question_"):
                question_id = int(key.split("_")[1])
                question = Question.objects.get(id=question_id)
                Answer.objects.create(user=user, question=question, score=int(value))

        return render(request, 'core/results.html')

    questions = Question.objects.all()
    return render(request, 'core/personality.html', {'questions': questions})


@login_required
def quiz_results(request):
    results = Result.objects.filter(user=request.user)
    return render(request, 'core/results.html', {'results': results})

def calculate_results(user):
    traits = ['O', 'C', 'E', 'A', 'N']
    for trait in traits:
        answers = Answer.objects.filter(user=user, question__category=trait)
        score = sum(answer.score for answer in answers)
        Result.objects.create(user=user, trait=trait, score=score)

@login_required
def take_aptitude_test(request):
    if request.method == 'POST':
        form = AptitudeForm(request.POST)
        if form.is_valid():
            for question_id, answer in form.cleaned_data.items():
                AptitudeAnswer.objects.create(
                    user=request.user,
                    question=AptitudeQuestion.objects.get(pk=question_id),
                    text=answer,
                    score=calculate_score(answer)
                )
            return redirect('aptitude_result')
    else:
        form = AptitudeForm()
    return render(request, 'aptitude.html', {'form': form})

@login_required
def aptitude_result(request):
    result = AptitudeAnswer.objects.filter(user=request.user).latest('id')
    context = {'result': result}
    return render(request, 'aptitude_result.html', context)
