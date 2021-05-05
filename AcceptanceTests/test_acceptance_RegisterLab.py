from django.test import TestCase, Client
from project_app.models import Course,Section,User


class SupCourseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(courseid="361", name="Software Engineering",credits=3)
        self.lab = Section.objects.create(course= self.course, sectionid="901", type="Lab",
                                            schedule="T @ 11:00 - 12:50")
        self.loginuser = User.objects.create(username="user23", name="user23", password="123", email="nub@uwm.edu",
                                             role="supervisor")

    def test_SectionExists(self):
        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/", {"section_sectionid": self.lab.sectionid, "type": self.lab.type,
                                                      "section_schedule": self.lab.schedule})
        self.assertEqual(response.context["message"], "Section with that ID already exists", msg="Section created twice")

    def test_createsection(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/", {"section_sectionid": "902", "type": "Lab", "section_schedule": "R @ 11:00 - 12:50"})
        self.assertEqual(response.url, '/Courses/')

        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/",
                                    {"section_sectionid": "903", "type": "Lab", "section_schedule": "R @ 11:00 - 12:50"}, follow=True)
        self.assertEqual(len(response.context["dictionary"][self.course]), 3)

    def test_emptySectionid(self):
        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/", {"section_sectionid": "", "type": "Lab", "section_schedule": "R @ 11:00 - 12:50"})
        self.assertEqual(response.context["message"], "Please fill out all required entries",
                         msg="Empty id, section created without id")

    def test_emptySectionname(self):
        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/", {"section_sectionid": "902", "type": "", "section_schedule": "R @ 11:00 - 12:50"})
        self.assertEqual(response.context["message"], "Please fill out all required entries",
                         msg="Empty name, lab created without name")

    def test_emptySectionschedule(self):
        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/", {"section_sectionid": "902", "type": "lab", "section_schedule": ""})
        self.assertEqual(response.context["message"], "Please fill out all required entries",
                         msg="Empty schedule, lab created without schedule")
