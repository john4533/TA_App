from django.test import TestCase, Client
from project_app.models import User, Course, Section



class SupCoursesTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(courseid="361", name="Software Engineering",credits=3)
        self.lab = Section.objects.create(course=self.course, sectionid="901", type="Lab", schedule="T @ 11:00 - 12:50")
        self.loginuser = User.objects.create(username="user23", name="user23", password="123", email="nub@uwm.edu",
                                             role="supervisor")

    def test_add_lab(self):
        response = self.client.post("/Courses/", {"register_section": "register_section"})
        self.assertEqual(response.url, "/RegisterSection/")

    def test_add_course(self):
        response = self.client.post("/Courses/", {"add_course": "add_course"})
        self.assertEqual(response.url, "/RegisterCourses/")

    def test_delete_course(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        self.assertEqual(len(list(Course.objects.all())), 1)
        response = self.client.post("/Courses/", {"delete_course": self.course.courseid})
        self.assertEqual(len(list(Course.objects.all())), 0)
        self.assertEqual(response.context["message"], "Course with ID 361 has been deleted")

    def test_delete_Section(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        self.assertEqual(len(list(Section.objects.all())), 1)
        response = self.client.post("/Courses/", {"del_section": self.lab.sectionid})
        self.assertEqual(len(list(Section.objects.all())), 0)
        self.assertEqual(response.context["message"], "Section with ID 901 has been deleted")
