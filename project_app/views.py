from django.shortcuts import render, redirect
from django.views import View
from .models import Users
from Classes.user import User
from Classes.functions import *
# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,"login.html",{})
    def post(self,request):
        result = login(request.POST['name'], request.POST['password'])
        if not result:
            return render(request,"login.html",{"message":"username or password is incorrect"})
        else:
            request.session["name"] = request.POST['name']
            return redirect("/things/")

