from django.test import TestCase, Client
from project_app.models import User, Course,Section,TA


class TestAssign(TestCase):

    def setUp(self):
        self.course = Course.objects.create(courseid="361", name="Software Engineering", credits=3)
        self.loginuser = User.objects.create(username="user23", name="user23", password="123", email="nub@uwm.edu",
                                             role="supervisor")
        self.course1 = Course.objects.create(courseid="122", name="System Design", credits=3)
        self.lab = Section.objects.create(course=self.course, sectionid="901", type="Lab",
                                          )
        self.lec = Section.objects.create(course=self.course, sectionid="902", type="Lecture",
                                          schedule="T @ 11:00 - 12:50")
        self.Ins1 = User.objects.create(username="user2", name="user2", password="123", email="nub@uwm.edu",
                                             role="Instructor")
        self.ta = User.objects.create(username="user3", name="user3", password="123", email="nub@uwm.edu",
                                        role="TA")
        self.ta1=TA.objects.create(user=self.ta,graderstatus=False,numlabs="1")

    def test_AssignCourseInstructor(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/RegisterCourses/", {"cor_name": "xya", "cor_id": "1",
                                                          "cor_cred": "3"})
        self.assertEqual(response.url,'/Courses/')
        self.client.post("/Courses/",{"assign_instructor":"1"})
        response=self.client.post("/AssignInstructor/", {"instructor":self.Ins1.username})
        self.assertEqual(response.url,"/Courses/")

    def test_AssignCourseTA(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/RegisterCourses/", {"cor_name": "xya", "cor_id": "1",
                                                          "cor_cred": "3"})
        self.assertEqual(response.url, '/Courses/')
        self.client.post("/Courses/", {"register_section": "1"}, follow=True)
        response = self.client.post("/RegisterSection/", {"section_sectionid": "102", "type": "Lab",
                                                          "section_schedule": "R @ 11:00 - 12:50"})
        self.assertEqual(response.url, '/Courses/')
        self.client.post("/Courses/", {"assign_TA_to_course": "1"})
        response = self.client.post("/AssignTAToCourse/", {"UserName": self.ta1.user.username, "numLabs":"1"})
        self.assertEqual(response.url, "/Courses/")

    def test_AssignTAToSection(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/RegisterCourses/", {"cor_name": "xya", "cor_id": "1",
                                                          "cor_cred": "3"})
        self.assertEqual(response.url, '/Courses/')
        self.client.post("/Courses/", {"register_section": "1"}, follow=True)
        response = self.client.post("/RegisterSection/", {"section_sectionid": "102", "type": "Lab",
                                                          "section_schedule": "R @ 11:00 - 12:50"})
        self.assertEqual(response.url, '/Courses/')
        self.client.post("/Courses/", {"assign_TA_to_course": "1"})
        response = self.client.post("/AssignTAToCourse/", {"UserName": self.ta1.user.username, "numLabs": "1"})
        self.assertEqual(response.url, "/Courses/")

        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/", {"section_sectionid": "145", "type": "Lab",
                                                          "section_schedule": "R @ 11:00 - 12:50"})
        self.assertEqual(response.url, '/Courses/')

        self.client.post("/Courses/",{"assign_TA_to_Section":"145" })
        response=self.client.post("/AssignTAToSection/",{"username":self.ta1.user.username})
        self.assertEqual("/Courses/",response.url)