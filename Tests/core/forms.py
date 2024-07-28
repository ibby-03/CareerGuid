<<<<<<< HEAD
# core/forms.py

from django import forms
from .models import Question
from .models import AptitudeQuestion, AptitudeAnswer

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[
                    (1, 'Strongly Disagree'),
                    (2, 'Disagree'),
                    (3, 'Neutral'),
                    (4, 'Agree'),
                    (5, 'Strongly Agree')
                ],
                widget=forms.RadioSelect
            )

class AptitudeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AptitudeForm, self).__init__(*args, **kwargs)
        questions = AptitudeQuestion.objects.all()
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[(answer.id, answer.text) for answer in question.aptitudeanswer_set.all()],
                widget=forms.RadioSelect,
                required=True
            )
=======
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
        

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


>>>>>>> 4b7d9095c2b05a05d3d9aadbbec3c126137eee1d

