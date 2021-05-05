from django.test import TestCase, Client
from project_app.models import User, Course


class SupCourseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(courseid="361",name="Software Engineering",credits=3)
        self.loginuser = User.objects.create(username="user23", name="user23", password="123", email="nub@uwm.edu",
                                             role="supervisor")

    def test_courseExists(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/RegisterCourses/", {"cor_name": self.course.name,"cor_id": self.course.courseid,
                                    "cor_cred": self.course.credits})
        self.assertEqual(response.context["message"], "Course with that ID already exists", msg="Course created twice")

    def test_createCourse(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/RegisterCourses/", {"cor_id": "337", "cor_name": "System Programming", "cor_cred": "3"})
        self.assertEqual(response.url, '/Courses/')

        response = self.client.post("/RegisterCourses/",
                                    {"cor_id": "338", "cor_name": "System Programming",
                                     "cor_cred": "3"}, follow=True)
        self.assertEqual(len(response.context["dictionary"]), 3)

    def test_emptyCourseid(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/RegisterCourses/", {"cor_id": "", "cor_name": "System Programming","cor_cred": "3"})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty id, course created without id")

    def test_emptyCoursename(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/RegisterCourses/", {"cor_id": "337", "cor_name": "","cor_cred": "3"})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty name, course created without name")


    def test_emptyCoursecredits(self):
        response = self.client.post("/RegisterCourses/", {"cor_id": "337", "cor_name": "System Programming","cor_cred": ""})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty credits, course created without credits")
