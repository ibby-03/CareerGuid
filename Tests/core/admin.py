# core/admin.py

from django.contrib import admin
from .models import Question, Answer, Result

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)

