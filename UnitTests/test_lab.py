from django.test import TestCase
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from project_app.models import User, Lab, Course
from Classes.functions import *

class MyTestCase(TestCase):

    def setUp(self):
        self.lab1 = Lab.objects.create(labid="902", labname="Software Engineering Lab 2", labschedule="R @ 11:00 - 12:50")

#   CREATE COURSE TESTS
    def test_labIdexists(self):
        self.assertEqual(createLab("902", "Software Engineering Lab 1", "T @ 11:00 - 12:50"),
                         "Lab with that ID already exists")

    def test_labCreated(self):
        createLab("901", "Software Engineering Lab 1", "T @ 11:00 - 12:50")
        b = Lab.objects.get(labid="901")
        self.assertEqual("Software Engineering Lab 1", b.labname)
        self.assertEqual("R @ 11:00 - 12:50", b.labschedule)

    def test_nolabid(self):
        self.assertEqual(createLab("", "Software Engineering Lab 1", "R @ 11:00 - 12:50"),
                         "Please fill out all required entries")

    def test_nolabename(self):
        self.assertEqual(createCourse("901", "", "R @ 11:00 - 12:50"), "Please fill out all required entries")

    def test_nolabschedule(self):
        self.assertEqual(createCourse("901", "Software Engineering Lab 1", ""), "Please fill out all required entries")


#   DELETE LAB TESTS
    def test_deletenolabidentered(self):
        self.assertEqual(deleteLab(""), "Please enter a course ID")

    def test_deletenolabexists(self):
        self.assertEqual(deleteLab("901"), "Course with that ID does not exist")

    def test_deletelab(self):
        self.assertEqual(self.lab1.labid, "902")
        self.assertEqual(deleteLab("902"), "Course with ID 902 has been deleted")



#     # invalid input
#     def test_noLabId(self):
#         with self.assertRaises(TypeError, msg="Need to input Lab ID"):
#             createLab(None, "Introduction to Software Engineering Lab")
#
#     def test_noLabName(self):
#         with self.assertRaises(TypeError, msg="Need to input Lab Name"):
#             createLab("361-901", None)
#
#     # createLab()
#     def test_createLab(self):
#         a = createLab("361-901", "Introduction to Software Engineering Lab")
#         b = Lab.objects.get(labid="361-901")
#         self.assertEqual("361-901", b.labid)
#         self.assertEqual("Introduction to Software Engineering Lab", b.labname)
#
#     def test_createLab_alreadyExists(self):
#         a = createLab("361-901", "Introduction to Software Engineering Lab")
#         b = Lab.objects.get(labid="361-901")
#         with self.assertRaises(TypeError, msg="The Lab with that ID already exists"):
#             createLab("361-901", "Introduction to Software Engineering Lab")
#
#     #setLabId()
#     def test_setLabId(self):
#         a = createLab("361-901", "Introduction to Software Engineering Lab")
#         setLabId("361-902", "361-901")
#         b = Lab.objects.get(labid="361-902")
#         self.assertEqual("Introduction to Software Engineering Lab", b.labname)
#
#     def test_setLabId_labDoesNotExist(self):
#         with self.assertRaises(TypeError, msg="The Lab with that original ID does not exist"):
#             setLabId("361-902", "361-901")
#
#     def test_setLabId_idAlreadyExists(self):
#         a = createLab("361-901", "Introduction to Software Engineering Lab")
#         b = createLab("361-902", "Introduction to Software Engineering Lab")
#         with self.assertRaises(TypeError, msg="The new Lab ID already exists"):
#             setLabId("361-902", "361-901")
#
#     # setLabName()
#     def test_setLabName(self):
#         a = createLab("361-901", "Introduction to Software Engineering Lab")
#         setLabName("New Lab Name", "361-901")
#         b = Lab.objects.get(labid="361-901")
#         self.assertEqual("New Lab Name", b.labname)
#
#     def test_setLabName_labDoesNotExist(self):
#         with self.assertRaises(TypeError, msg="The Lab with that ID does not exist"):
#             setLabName("New Lab Name", "361-901")
#
#     # setLabSchedule()
#     def test_setLabSechedule(self):
#         a = createLab("361-901", "Introduction to Software Engineering Lab")
#         setLabSchedule("TR - 10:00", "361-901")
#         b = Lab.objects.get(labid="361-901")
#         self.assertEqual("TR - 10:00", b.schedule)
#
#     def test_setLabSchedule_labDoesNotExist(self):
#         with self.assertRaises(TypeError, msg="The Lab with that ID does not exist"):
#             setLabSchedule("TR - 10:00", "361-901")
#
#     # setLabTA()
#     def test_setLabTA(self):
#         a = createLab("361-901", "Introduction to Software Engineering Lab")
#         setLabTA("Apoorv Prasad", "361-901")
#         b = Lab.objects.get(labid="361-901")
#         self.assertEqual("Apoorv Prasad", b.labTA)
#
#     def test_setLabTA_labDoesNotExist(self):
#         with self.assertRaises(TypeError, msg="The Lab with that ID does not exist"):
#             setLabTA("Apoorv Prasad", "361-901")
#
# if __name__ == '__main__':
#     unittest.main()
