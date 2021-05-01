from django.shortcuts import render, redirect
from django.views import View
from Classes.functions import *


# Create your views here.
class Login(View):
    def get(self, request):
        request.session["name"] = ""
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
        return render(request, "home.html", {})


class RegisterAccount(View):
    def get(self, request):
        return render(request, "register_account.html", {"roles": Roles.choices})

    def post(self, request):
        message = createAccount(request.POST['username'], request.POST['password'], request.POST['email'],
                                request.POST['role'], request.POST.get('phone'), request.POST.get('address'),
                                request.POST.get('officehours'))
        if message is "":
            return redirect('/AccountDisplay/')
        else:
            return render(request, "register_account.html", {"roles": Roles.choices, "message": message})



class RegisterCourses(View):
    def get(self, request):
        return render(request, "register_courses.html")

    def post(self, request):
        message = createCourse(request.POST['cor_id'], request.POST['cor_name'], request.POST['cor_cred'])
        if message is "":
            return redirect('/SupCourses/')
        else:
            return render(request, "register_courses.html", {"message": message})



class AccountDisplay(View):
    def get(self, request):
        user = User.objects.get(username=request.session["name"])
        return render(request, "all_accounts.html", {"accounts": list(User.objects.exclude(role="Supervisor")), "user":user})

    def post(self, request):
        user = User.objects.get(username=request.session["name"])
        if request.POST.get('delete_account'):
            message = deleteAccount(request.POST['delete_account'])
            return render(request, "all_accounts.html",
                          {"accounts": list(User.objects.exclude(role="Supervisor")), "delete_message": message,"user":user})
        else:
            return redirect('/RegisterAccount/')


class SupCourses(View):
    def get(self, request):
        return render(request, "sup_courses.html", {"dictionary": getCourses()})

    def post(self, request):
        if request.POST.get('add_course'):
            return redirect('/RegisterCourses/')
        elif request.POST.get('add_section'):
            request.session["course"] = request.POST["add_section"]
            return redirect('/RegisterSection/')
        else:
            if request.POST.get('delete_course'):
                message = deleteCourse(request.POST['delete_course'])
            elif request.POST.get('delete_section'):
                message = deleteSection(request.POST['delete_section'])
            return render(request, "sup_courses.html", {"dictionary": getCourses(), "delete_message": message},)


class RegisterSection(View):
    def get(self, request):
        return render(request, "register_section.html", {"types": Types.choices})

    def post(self, request):
        message = createSection(Course.objects.get(courseid=request.session["course"]),
                                request.POST['section_sectionid'], request.POST['type'],
                                request.POST['section_schedule'])
        if message is "":
            request.session["course"] = ""
            return redirect('/SupCourses/')
        else:
            return render(request, "register_section.html", {"types": Types.choices, "message": message})


class Account(View):
    def get(self, request):
        user = User.objects.get(username=request.session["name"])
        return render(request, "account.html", {"user": user})
