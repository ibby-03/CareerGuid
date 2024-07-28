from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import auth
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Existing views
def testers(request):
    return render(request, 'core/testers.html')

def personality(request):
    return render(request, 'core/personality.html')

def aptitude(request):
    return render(request, 'core/aptitude.html')

def signin(request):
    context = {}
    return render(request, 'core/signin.html', context)

def createaccount(request):
    context = {}
    return render(request, 'core/createaccount.html', context)

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

<<<<<<< HEAD
def roadmappageresults(request):
    return render(request, 'core/roadmappageresults.html')
=======
# New views for Firebase authentication
@csrf_exempt
class SignUpView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        try:
            user_record = auth.create_user(email=email, password=password)
            return JsonResponse({'uid': user_record.uid}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
class LoginView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        try:
            user = auth.get_user_by_email(email)
            id_token = auth.create_custom_token(user.uid)
            user = authenticate(request, uid=user.uid)
            if user is not None:
                login(request, user)
                return JsonResponse({'id_token': id_token.decode('utf-8')}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> a292e44f15292224610bfd12345b7f0e881dc527
