from django.test import TestCase, Client
from project_app.models import User, Course, Lab


class SupCoursesTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(courseid="361", coursename="Software Engineering", courseschedule="TR @ 10:00 - 10:50", coursecredits=3)
        self.lab = Lab.objects.create(course=self.course, labid="901", labname="Lab 1", labschedule="T @ 11:00 - 12:50")

    def test_add_lab(self):
        response = self.client.post("/SupCourses/", {"add_lab": "add_lab"})
        self.assertEqual(response.url, "/RegisterLab/")

    def test_add_course(self):
        response = self.client.post("/SupCourses/", {"add_course": "add_course"})
        self.assertEqual(response.url, "/RegisterCourses/")

    def test_delete_course(self):
        self.assertEqual(len(list(Course.objects.all())), 1)
        response = self.client.post("/SupCourses/", {"delete_course": self.course.courseid})
        self.assertEqual(len(list(Course.objects.all())), 0)
        self.assertEqual(response.context["delete_message"], "Course with ID 361 has been deleted")

    def test_delete_lab(self):
        self.assertEqual(len(list(Lab.objects.all())), 1)
        response = self.client.post("/SupCourses/", {"delete_lab": self.lab.labid})
        self.assertEqual(len(list(Lab.objects.all())), 0)
        self.assertEqual(response.context["delete_message"], "Lab with ID 901 has been deleted")
