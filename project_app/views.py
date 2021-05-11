from django.shortcuts import render, redirect
from django.views import View
from Classes.functions import *
from datetime import datetime


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
            return redirect('/Home/')


class Home(View):
    def get(self, request):
        return render(request, "home.html", {})


class Account(View):
    def get(self, request):
        user = User.objects.get(username=request.session["name"])
        return render(request, "account.html", {"user": user})

    def post(self, request):
        request.session["name"] = request.POST["edit_account"]
        return redirect('/editAccount/')


class EditAccount(View):
    def get(self, request):
        user = User.objects.get(username=request.session["name"])
        return render(request, "edit_account.html", {"user": user, "days": Days.choices})

    def post(self, request):

        print

        message = editAccount(request.POST['update_account'],
                            request.POST.get('name'), request.POST.get('password'), request.POST.get('address'),
                            request.POST.get('phone'), request.POST.get('officenumber'),
                            request.POST.get('officehoursStart'), request.POST.get('officehoursEnd'),
                            request.POST.getlist('selectedDays'), request.POST.get('skills'))
        if message!="":
            return render(request, "edit_account.html", {"roles": Roles.choices, "message": message})

        elif request.session["name"]==request.POST['update_account']:
            return redirect('/Account/')
        else:
            return redirect('/AccountDisplay/')


class AccountDisplay(View):
    def get(self, request):
        user = User.objects.get(username=request.session["name"])
        return render(request, "all_accounts.html",
                      {"accounts": list(User.objects.exclude(role="Supervisor")), "user": user})

    def post(self, request):
        if request.POST.get('edit_account'):
            user=User.objects.get(username=request.POST['edit_account'])
            return render(request, "edit_account.html", {"user": user, "days": Days.choices})
        if request.POST.get('delete_account'):
            message = deleteAccount(request.POST['delete_account'])
            return render(request, "all_accounts.html",
                          {"accounts": list(User.objects.exclude(role="Supervisor")), "delete_message": message,
                           "role": "Supervisor"})
        else:
            return redirect('/RegisterAccount/')


class RegisterAccount(View):
    def get(self, request):
        return render(request, "register_account.html", {"roles": Roles.choices, "days": Days.choices})

    def post(self, request):
        message = createAccount(request.POST['username'], request.POST['name'], request.POST['password'], request.POST['email'],
                                request.POST['role'], request.POST.get('phone'), request.POST.get('address'),
                                request.POST.get('officenumber'), request.POST.get('officehoursStart'), request.POST.get('officehoursEnd'),
                                request.POST.getlist('selectedDays'), request.POST.get('skills'))

        if message.__eq__(""):
            return redirect('/AccountDisplay/')
        else:
            return render(request, "register_account.html", {"roles": Roles.choices, "days": Days.choices, "message": message})


class Courses(View):
    def get(self, request):
        user = User.objects.get(username=request.session["name"])
        return render(request, "all_courses.html", {"dictionary": getCourses(),
                                                    "TAs": list(TA.objects.all()), "user": user})

    def post(self, request):
        if request.POST.get('add_course'):
            return redirect('/RegisterCourses/')
        elif request.POST.get('assign_instructor'):
            request.session["course"] = request.POST["assign_instructor"]
            return redirect('/AssignInstructor/')
        elif request.POST.get('register_section'):
            request.session["course"] = request.POST["register_section"]
            return redirect('/RegisterSection/')
        elif request.POST.get('assign_TA_to_course'):
            request.session["course"] = request.POST["assign_TA_to_course"]
            return redirect('/AssignTAToCourse/')
        elif request.POST.get('assign_TA_to_Section'):
            request.session["sectionid"] = request.POST["assign_TA_to_Section"]
            return redirect('/AssignTAToSection/')
        else:
            message = ""
            if request.POST.get('delete_course'):
                message = deleteCourse(request.POST['delete_course'])
            if request.POST.get('rem_TA'):
                message = unAssignTA(request.POST['rem_TA'])
            elif request.POST.get('del_section'):
                message = deleteSection(request.POST['del_section'])
            elif request.POST.get('rem_TA_sec'):
                message = unAssignTASection(request.POST['rem_TA_sec'])
            elif request.POST.get('rem_Ins'):
                message = unAssignInstructor(request.POST['rem_Ins'])

            user = User.objects.get(username=request.session["name"])
            return render(request, "all_courses.html", {"dictionary": getCourses(),
                                                        "TAs": list(TA.objects.all()), "message": message,
                                                        "user": user})


class RegisterCourses(View):
    def get(self, request):
        return render(request, "register_courses.html")

    def post(self, request):
        message = createCourse(request.POST['cor_id'], request.POST['cor_name'], request.POST['cor_cred'])
        if message is "":
            return redirect('/Courses/')
        else:
            return render(request, "register_courses.html", {"message": message})


class RegisterSection(View):
    def get(self, request):
        return render(request, "register_section.html", {"types": Types.choices, "days": Days.choices})

    def post(self, request):
        message = createSection(Course.objects.get(courseid=request.session["course"]),
                                request.POST['section_sectionid'], request.POST['type'],
                                request.POST['scheduleStart'], request.POST['scheduleEnd'],
                                request.POST.getlist('selectedDays'))
        if message is "":
            request.session["course"] = ""
            return redirect('/Courses/')
        else:
            return render(request, "register_section.html", {"types": Types.choices, "days": Days.choices, "message": message})


class AssignInstructor(View):
    def get(self, request):
        return render(request, "assign_instructor.html",
                      {"accounts": list(User.objects.exclude(role="Supervisor").exclude(role="TA")), "totalacc": len(list(User.objects.exclude(role="Supervisor").exclude(role="TA")))})

    def post(self, request):
        message = assignInstructor(Course.objects.get(courseid=request.session["course"]),
                                   request.POST.get('instructor'))
        if message is "":
            return redirect('/Courses/')

        else:
            return render(request, "assign_instructor.html",
                          {"accounts": list(User.objects.exclude(role="Supervisor").exclude(role="TA")),
                            "totalacc": len(list(User.objects.exclude(role="Supervisor").exclude(role="TA"))), "message": message})


class AssignTAToCourse(View):
    def get(self, request):
        return render(request, "assign_TA_to_course.html", {"TAs": list(TA.objects.filter(course__isnull=True)), "totalTAs": len(list(TA.objects.filter(course__isnull=True)))})

    def post(self, request):
        message = assignTAtoCourse(Course.objects.get(courseid=request.session["course"]), request.POST.get('UserName'),
                                   request.POST.get('numLabs'), request.POST.get('graderStatus'))

        if message is "":
            request.session["course"] = ""
            return redirect('/Courses/')
        else:
            return render(request, "assign_TA_to_course.html", {"TAs": list(TA.objects.filter(course__isnull=True)), "totalTAs": len(list(TA.objects.filter(course__isnull=True))),
                                                                "message": message})


class AssignTAToSection(View):
    def get(self, request):
        return render(request, "assign_TA_to_section.html", {"TAs": getTAsInCourse(request.session["sectionid"]), "totalTAs": len(getTAsInCourse(request.session["sectionid"]))})

    def post(self, request):
        message = assignTAtoSection(request.session["sectionid"], request.POST.get('username'))

        if message is "":
            request.session["course"] = ""
            return redirect('/Courses/')

        else:
            return render(request, "assign_TA_to_section.html",
                          {"TAs": getTAsInCourse(request.session["sectionid"]),  "totalTAs": len(getTAsInCourse(request.session["sectionid"])), "message": message})
