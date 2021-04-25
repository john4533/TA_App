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
            return render(request, "login.html", {"message": "information is incorrect"})
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
                                request.POST['role'], request.POST['phone'], request.POST['address'], request.POST['officehours'])
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
        accounts = list(User.objects.all())
        return render(request, "account_display.html", {"accounts":accounts})

    def post(self, request):
        if request.POST.get('delete_account'):
            message = deleteAccount(request.POST['delete_account'])
            accounts = list(User.objects.all())
            return render(request, "account_display.html", {"accounts": accounts, "delete_message": message})
        else:
            return redirect('/RegisterAccount/')


class SupCourses(View):
    def get(self, request):
        courses = list(Course.objects.all())
        return render(request, "sup_courses.html", {"courses": courses})

    def post(self, request):
        if request.POST.get('delete_course'):
            message = deleteCourse(request.POST['delete_course'])
            courses = list(Course.objects.all())
            return render(request, "sup_courses.html", {"courses": courses, "delete_message": message})
        else:
            return redirect('/RegisterCourses/')

class CreateLab(View):
    def get(self, request):
        return render(request, "sup_create_lab.html")

class Account(View):
    def get(self,request):
        return render(request,"account.html")

class SupEmail(View):
    def get(self, request):
        return render(request, "sup_email.html", {})
