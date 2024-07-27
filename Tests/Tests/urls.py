"""
URL configuration for Tests project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import testers, personality, aptitude,signin ,createaccount,score, assessments

urlpatterns = [
    path('assessments/', assessments, name='assessments'),
    path('score/', score, name='score'),
    path('createaccount/', createaccount, name='createaccount'),
    path('signin/', signin, name='signin'),
    path('aptitude/', aptitude, name='aptitude' ),
    path('personality/', personality, name='personality'),
    path('', testers, name='testers'),
    path('admin/', admin.site.urls),
]
