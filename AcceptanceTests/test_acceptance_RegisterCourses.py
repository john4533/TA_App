from django.test import TestCase, Client
from project_app.models import User, Course


class SupCourseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(courseid="361", coursename="Software Engineering", courseschedule="TR @ 10:00 - 10:50", coursecredits=3)

    def test_courseExists(self):
        response = self.client.post("/RegisterCourses/", {"cor_id": self.course.courseid, "cor_name": self.course.coursename,
                                    "cor_sched": self.course.courseschedule, "cor_cred": self.course.coursecredits})
        self.assertEqual(response.context["message"], "Course with that ID already exists", msg="Course created twice")

    def test_createCourse(self):
        response = self.client.post("/RegisterCourses/", {"cor_id": "337", "cor_name": "System Programming", "cor_sched": "TR @ 1:00 - 1:50", "cor_cred": "3"})
        self.assertEqual(response.url, '/SupCourses/')

        response = self.client.post("/RegisterCourses/",
                                    {"cor_id": "338", "cor_name": "System Programming", "cor_sched": "TR @ 1:00 - 1:50",
                                     "cor_cred": "3"}, follow=True)
        self.assertEqual(len(response.context["dictionary"]), 3)

    def test_emptyCourseid(self):
        response = self.client.post("/RegisterCourses/", {"cor_id": "", "cor_name": "System Programming", "cor_sched": "TR @ 1:00 - 1:50", "cor_cred": "3"})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty id, course created without id")

    def test_emptyCoursename(self):
        response = self.client.post("/RegisterCourses/", {"cor_id": "337", "cor_name": "", "cor_sched": "TR @ 1:00 - 1:50", "cor_cred": "3"})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty name, course created without name")

    def test_emptyCourseschedule(self):
        response = self.client.post("/RegisterCourses/", {"cor_id": "337", "cor_name": "System Programming", "cor_sched": "", "cor_cred": "3"})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty schedule, course created without schedule")

    def test_emptyCoursecredits(self):
        response = self.client.post("/RegisterCourses/", {"cor_id": "337", "cor_name": "System Programming", "cor_sched": "TR @ 1:00 - 1:50", "cor_cred": ""})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty credits, course created without credits")
