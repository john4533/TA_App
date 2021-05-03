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
            return redirect('/Home/')


class Home(View):
    def get(self, request):
        return render(request, "home.html", {})


class Account(View):
    def get(self, request):
        user = User.objects.get(username=request.session["name"])
        return render(request, "account.html", {"user": user})


class AccountDisplay(View):
    def get(self, request):
        user = User.objects.get(username=request.session["name"])
        print(user)
        return render(request, "all_accounts.html",
                      {"accounts": list(User.objects.exclude(role="Supervisor")), "user": user})

    def post(self, request):
        if request.POST.get('delete_account'):
            message = deleteAccount(request.POST['delete_account'])
            return render(request, "all_accounts.html",
                          {"accounts": list(User.objects.exclude(role="Supervisor")), "delete_message": message,
                           "role": "Supervisor"})
        else:
            return redirect('/RegisterAccount/')


class RegisterAccount(View):
    def get(self, request):
        return render(request, "register_account.html", {"roles": Roles.choices})

    def post(self, request):
        message = createAccount(request.POST['username'], request.POST['name'], request.POST['password'],
                                request.POST['email'],
                                request.POST['role'], request.POST.get('phone'), request.POST.get('address'),
                                request.POST.get('officehours'))
        if message is "":
            return redirect('/AccountDisplay/')
        else:
            return render(request, "register_account.html", {"roles": Roles.choices, "message": message})


class Courses(View):
    def get(self, request):
        return render(request, "all_courses.html", {"dictionary": getCourses()})

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
        elif request.POST.get('Assign_TA_to_Section'):
            return redirect('/AssignTAToSection/')
        else:
            if request.POST.get('delete_course'):
                message = deleteCourse(request.POST['delete_course'])
            elif request.POST.get('delete_section'):
                message = deleteSection(request.POST['delete_section'])
            return render(request, "all_courses.html", {"dictionary": getCourses(), "delete_message": message}, )


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
        return render(request, "register_section.html", {"types": Types.choices})

    def post(self, request):
        message = createSection(Course.objects.get(courseid=request.session["course"]),
                                request.POST['section_sectionid'],
                                request.POST['type'],
                                request.POST['section_schedule'])
        if message is "":
            request.session["course"] = ""
            return redirect('/Courses/')
        else:
            return render(request, "register_section.html", {"types": Types.choices, "message": message})


class AssignInstructor(View):
    def get(self, request):
        return render(request, "assign_instructor.html",
                      {"accounts": list(User.objects.exclude(role="Supervisor").exclude(role="TA"))})

    def post(self, request):
        try:
            message = assignInstructor(Course.objects.get(courseid=request.session["course"]),
                                       request.POST['instructor'])
        except:
            message = "Please make a selection"
        if message is "":
            request.session["course"] = ""
            return redirect('/Courses/')

        else:
            return render(request, "assign_instructor.html",
                          {"accounts": list(User.objects.exclude(role="Supervisor").exclude(role="TA")),
                           "message": message})


class AssignTAToCourse(View):
    def get(self, request):
        return render(request, "assign_TA_to_course.html", dict(TAs=list(TA.objects.filter(course__isnull=True))))

    def post(self, request):
        try:
            message = assignTAtoCourse(Course.objects.get(courseid=request.session["course"]), request.POST['TA'],
                                       request.POST['numLabs'])
        except:
            message = "Please make a selection"
        if message is "":
            request.session["course"] = ""
            return redirect('/Courses/')
        else:
            return render(request, "assign_TA_to_course.html", {"TAs": list(TA.objects.filter(course__isnull=True)),
                                                                "message": message})


class AssignTAToSection(View):
    def get(self, request):
        return render(request, "assign_TA_to_section.html")
