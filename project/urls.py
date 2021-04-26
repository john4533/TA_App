"""TAproject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from project_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('SupHome/', SupHome.as_view()),
    path('SupCourses/', SupCourses.as_view()),
    path('Account/', Account.as_view()),
    path('RegisterCourses/', RegisterCourses.as_view()),
    path('RegisterLab/', RegisterLab.as_view()),
    path('RegisterAccount/',RegisterAccount.as_view()),
    path('AccountDisplay/',AccountDisplay.as_view()),
    path('', Login.as_view())
]



