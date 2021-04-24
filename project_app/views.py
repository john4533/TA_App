from urllib import request

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


class LogOut(View):
    def get(self, request):
        return render(request, "login.html", {})



class SupHome(View):
    def get(self, request):
        return render(request, "sup_home.html", {})


class SupAccounts(View):
    def get(self, request):
        accounts = list(User.objects.all())
        return render(request, "sup_accounts.html", {"roles": Roles.choices, "accounts": accounts})

    def post(self, request):
        message = createAccount(request.POST['username'], request.POST['password'], request.POST['email'],
                                request.POST['role'])
        accounts = list(User.objects.all())
        return render(request, "sup_accounts.html", {"roles": Roles.choices, "accounts": accounts, "message": message})


class SupCourses(View):
    def get(self, request):
        courses = list(Course.objects.all())
        return render(request, "sup_courses.html", {"courses": courses})

    def post(self, request):
        message = createCourse(request.POST['cor_id'], request.POST['cor_name'], request.POST['cor_sched'],
                               request.POST['cor_cred'])
        courses = list(Course.objects.all())
        return render(request, "sup_courses.html", {"courses": courses, "message": message})


class SupEmail(View):
    def get(self, request):
        return render(request, "sup_email.html", {})


class Account(View):
    def get(self, request):
        return render(request, "account.html", {})


class SupCourseView(View):
    def get(self, request):
        courses = list(Course.objects.all())
        return render(request, "sup_course_view.html", {"courses": courses})
