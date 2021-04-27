from django.test import TestCase, Client
from project_app.models import Course, Lab


class SupCourseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(courseid="361", coursename="Software Engineering", courseschedule="TR @ 10:00 - 10:50", coursecredits=3)
        self.lab = Lab.objects.create(course= self.course, labid="901", labname="Lab 1",
                                            labschedule="T @ 11:00 - 12:50")

    def test_labExists(self):
        self.client.post("/SupCourses/", {"add_lab": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterLab/", {"lab_id": self.lab.labid, "lab_name": self.lab.labname,
                                                      "lab_sched": self.lab.labschedule})
        self.assertEqual(response.context["message"], "Lab with that ID already exists", msg="Lab created twice")

    def test_createLab(self):
        self.client.post("/SupCourses/", {"add_lab": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterLab/", {"lab_id": "902", "lab_name": "Lab 2", "lab_sched": "R @ 11:00 - 12:50"})
        self.assertEqual(response.url, '/SupCourses/')

        self.client.post("/SupCourses/", {"add_lab": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterLab/",
                                    {"lab_id": "903", "lab_name": "Lab 2", "lab_sched": "R @ 11:00 - 12:50"}, follow=True)
        self.assertEqual(len(response.context["dictionary"][self.course]), 3)

    def test_emptyLabid(self):
        self.client.post("/SupCourses/", {"add_lab": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterLab/", {"lab_id": "", "lab_name": "Lab 2", "lab_sched": "R @ 11:00 - 12:50"})
        self.assertEqual(response.context["message"], "Please fill out all required entries",
                         msg="Empty id, lab created without id")

    def test_emptyLabname(self):
        self.client.post("/SupCourses/", {"add_lab": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterLab/", {"lab_id": "902", "lab_name": "", "lab_sched": "R @ 11:00 - 12:50"})
        self.assertEqual(response.context["message"], "Please fill out all required entries",
                         msg="Empty name, lab created without name")

    def test_emptyLabschedule(self):
        self.client.post("/SupCourses/", {"add_lab": self.course.courseid}, follow=True)
        response = self.client.post("/RegisterLab/", {"lab_id": "902", "lab_name": "Lab 2", "lab_sched": ""})
        self.assertEqual(response.context["message"], "Please fill out all required entries",
                         msg="Empty schedule, lab created without schedule")
