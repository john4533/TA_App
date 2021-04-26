from django.shortcuts import render, redirect
from django.views import View
from .models import User, Course
from Classes.functions import *

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        result = login(request.POST['name'], request.POST['password'])
        if not result:
            return render(request, "login.html", {"message": "Information is incorrect"})
        else:
            request.session["name"] = request.POST['name']
            return redirect('/SupHome/')


class SupHome(View):
    def get(self, request):
        return render(request, "sup_home.html", {})


class RegisterAccount(View):
    def get(self, request):
        return render(request, "register_account.html", {"roles": Roles.choices})

    def post(self, request):
        message = createAccount(request.POST['username'], request.POST['password'], request.POST['email'],
                                request.POST['role'], request.POST.get('phone'), request.POST.get('address'), request.POST.get('officehours'))
        if message is None:
            return redirect('/AccountDisplay/')
        else:
            return render(request, "register_account.html", {"roles": Roles.choices, "message": message})


class RegisterCourses(View):
    def get(self, request):
        return render(request, "register_courses.html")

    def post(self, request):
        message = createCourse(request.POST['cor_id'], request.POST['cor_name'], request.POST['cor_sched'], request.POST['cor_cred'])
        if message is None:
            return redirect('/SupCourses/')
        else:
            return render(request, "register_courses.html", {"message": message})

class AccountDisplay(View):
    def get(self, request):
        return render(request, "account_display.html", {"accounts":list(User.objects.exclude(role="Supervisor"))})

    def post(self, request):
        if request.POST.get('delete_account'):
            message = deleteAccount(request.POST['delete_account'])
            return render(request, "account_display.html", {"accounts": list(User.objects.exclude(role="Supervisor")), "delete_message": message})
        else:
            return redirect('/RegisterAccount/')


class SupCourses(View):
    def get(self, request):
        dictionary = getCourses()
        return render(request, "sup_courses.html", {"dictionary": dictionary})

    def post(self, request):
        if request.POST.get('add_course'):
            return redirect('/RegisterCourses/')
        elif request.POST.get('add_lab'):
            request.session["course"] = request.POST["add_lab"]
            return redirect('/RegisterLab/')
        if request.POST.get('delete_course'):
            message = deleteCourse(request.POST['delete_course'])
        elif request.POST.get('delete_lab'):
            message = deleteLab(request.POST['delete_lab'])
        return render(request, "sup_courses.html", {"dictionary": getCourses(), "delete_message": message})


class RegisterLab(View):
    def get(self, request):
        return render(request, "register_lab.html")

    def post(self, request):
        message = createLab(Course.objects.get(courseid=request.session["course"]), request.POST['lab_id'], request.POST['lab_name'], request.POST['lab_sched'])
        if message is None:
            request.session["course"] = ""
            return redirect('/SupCourses/')
        else:
            return render(request, "register_lab.html", {"message": message})

class Account(View):
    def get(self,request):
        user = User.objects.get(username=request.session["name"])
        return render(request,"account.html",{"user":user})

# class SupEmail(View):
#     def get(self, request):
#         return render(request, "sup_email.html", {})
