from django.shortcuts import render, redirect
from django.views import View
from .models import User
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
            return redirect('/SupCourses/')


# class CreateCourse(View):
#     def get(self, request):
#         return render(request, "CreateCourse.html", {})
#
#     def post(self, request):
#         result = CreateCourse(request.POST['courseid'], request.POST['coursename'])
#         if not result:
#             return render(request, "createcourse.html", {"message": "must enter a unique course id and a course name"})
#         else:
#
#             return


class SupHome(View):
    def get(self, request):
        return render(request, "sup_home.html", {})


class SupAccounts(View):
    def get(self, request):
        return render(request, "sup_accounts.html", {})


class SupCourses(View):
    def get(self, request):
        courses = Course.objects.all
        return render(request, "sup_courses.html", {"courses": courses})

    def post(self, request):
        coursename = request.POST.get('cor_name', '')
        courseid = request.POST.get('cor_id', '')
        courseschedule = request.POST.get('cor_sched', '')
        coursecredits = request.POST.get('cor_cred', '')
        print(coursename)
        print(courseid)
        print(courseschedule)
        print(coursecredits)
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
