from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from core.views import testers, personality, aptitude,signin ,createaccount,score, assessments, currenttrends, homepage, roadmappage, roadmappageresults
from core.forms import LoginForm 

urlpatterns = [
    path('assessments/', assessments, name='assessments'),
    path('score/', score, name='score'),
    path('createaccount/', createaccount, name='createaccount'),
    path('signin/', signin, name='signin'),
    path('aptitude/', aptitude, name='aptitude' ),
    path('personality/', personality, name='personality'),
    path('', testers, name='testers'),
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name='homepage'),
    path('currenttrends/', currenttrends, name='currenttrends'),
    path('roadmappage/', roadmappage, name='roadmappage'),
    path('roadmappageresults/', roadmappageresults, name='roadmappageresults'),
]
