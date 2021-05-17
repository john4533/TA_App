from django.test import TestCase, Client
from project_app.models import Course,Section,User


class SupCourseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(courseid="361", name="Software Engineering",credits=3)
        self.lab = Section.objects.create(course= self.course, sectionid="901", type="Lab",
                                            scheduleStart="11:00", scheduleEnd="12:00", scheduleDays=["Thursday","Tuesday"])
        self.loginuser = User.objects.create(username="user23", name="user23", password="123", email="nub@uwm.edu",
                                             role="supervisor")

    def test_SectionExists(self):
        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/course/", {"section_sectionid": self.lab.sectionid, "type": self.lab.type,
                                                          "section_scheduleStart":self.lab.scheduleStart,"section_scheduleEnd":self.lab.scheduleEnd,
                                                          "section_scheduleDays":self.lab.scheduleDays})

    def test_createsection(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/", {"section_sectionid": "902", "type": "Lab",
                                                          "scheduleStart":self.lab.scheduleStart,
                                                          "scheduleEnd":self.lab.scheduleEnd,
                                                          "selectedDays":self.lab.scheduleDays})
        self.assertEqual(response.url,'/Courses/')

        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/",
                                    {"section_sectionid": "903", "type": "Lab", "scheduleStart":self.lab.scheduleStart,
                                                          "scheduleEnd":self.lab.scheduleEnd,
                                                          "selectedDays":self.lab.scheduleDays}, follow=True)
        self.assertEqual(len(response.context["dictionary"][self.course]), 3)

    def test_emptySectionid(self):
        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/", {
                                            "section_sectionid": "", "type": "Lab",  "scheduleStart":self.lab.scheduleStart,
                                                          "scheduleEnd":self.lab.scheduleEnd,
                                                          "scheduleDays":self.lab.scheduleDays})
        self.assertEqual(response.context["message"], "Please fill out all required entries",
                         msg="Empty id, section created without id")

    def test_emptySectionTyper(self):
        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/", {"section_sectionid": "902", "type": "",  "scheduleStart":self.lab.scheduleStart,
                                                          "scheduleEnd":self.lab.scheduleEnd,
                                                          "selectedDays":self.lab.scheduleDays})
        self.assertEqual(response.context["message"], "Please fill out all required entries",
                         msg="Please fill out all required entries")

    def test_emptySectionschedule(self):
        self.client.post("/Courses/", {"register_section": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterSection/", {"section_sectionid": "902", "type": "lab","scheduleStart":"",
                                                          "scheduleEnd":self.lab.scheduleEnd,
                                                          "selectedDays":self.lab.scheduleDays})
        self.assertEqual(response.context["message"], "Please fill out all required entries")

