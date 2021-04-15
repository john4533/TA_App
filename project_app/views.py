from django.shortcuts import render, redirect
from django.views import View
from .models import Users
from Classes.user import User
# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,"login.html",{})
    def post(self,request):
        noSuchUser = False
        badPassword = False
        try:
            m = Users.objects.get(name=request.POST['name'])
            badPassword = (m.password != request.POST['password'])
        except:
            noSuchUser = True
        if noSuchUser:
            return render(request,"login.html",{"message":"username does not exist"})
        elif badPassword:
            return render(request,"login.html",{"message":"incorrect password"})
        else:
            request.session["name"] = m.name
            return redirect("/things/")
