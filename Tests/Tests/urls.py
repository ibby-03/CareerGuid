from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

<<<<<<< HEAD
from core.views import testers, personality, aptitude,signin ,createaccount,score, assessments, currenttrends, homepage, roadmappage, roadmappageresults
=======
from core.views import testers, personality, aptitude, signin, createaccount, score, assessments, currenttrends, homepage, roadmappage, SignUpView, LoginView
>>>>>>> a292e44f15292224610bfd12345b7f0e881dc527
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
<<<<<<< HEAD
    path('roadmappageresults/', roadmappageresults, name='roadmappageresults'),
=======
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
>>>>>>> a292e44f15292224610bfd12345b7f0e881dc527
]
