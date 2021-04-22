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


class SupAccounts(View):
    def get(self, request):
        return render(request, "sup_accounts.html", {"roles": Roles.choices})

    def post(self, request):
        no_such_user = False

        user_lst = list(User.objects.filter(email=request.POST['email']))

        if user_lst.__len__() == 0:
            no_such_user = True

        if no_such_user:
            n = request.POST['username']
            p = request.POST['password']
            e = request.POST['email']
            print(e)
            r = request.POST['role']
            print(r)

            User.objects.create(username=n, password=p, email=e, role=r)
            return render(request, "sup_accounts.html", {"roles": Roles.choices})

        else:
            return render(request, "sup_accounts.html", {"roles": Roles.choices, "message": "this user already exists"})


class SupCourses(View):
    def get(self, request):
        courses = Course.objects.all
        return render(request, "sup_courses.html", {"courses": courses})

    def post(self, request):
        coursename = request.POST.get('cor_name', '')
        courseid = request.POST.get('cor_id', '')
        courseschedule = request.POST.get('cor_sched', '')
        coursecredits = request.POST.get('cor_cred', '')
        if coursename != '' and courseid != '' and courseschedule != '' and coursecredits != '':
            newCourse = Course(courseid=courseid, coursename=coursename, courseschedule=courseschedule, coursecredits=coursecredits)
            newCourse.save()
        courses = Course.objects.all
        return render(request, "sup_courses.html", {"courses": courses})

class SupEmail(View):
    def get(self, request):
        return render(request, "sup_email.html", {})


class Account(View):
    def get(self, request):
        return render(request, "account.html", {})
