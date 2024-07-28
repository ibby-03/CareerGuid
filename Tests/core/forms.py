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

