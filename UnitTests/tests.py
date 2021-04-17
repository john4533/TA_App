import unittest
import os
import django
from Classes.functions import createCourse, setCourseId, setCourseName, setCourseSchedule, setCourseCredits
from project_app.models import Course

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)


