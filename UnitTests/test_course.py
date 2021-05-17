from django.test import TestCase
import os
from Classes.functions import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
import project_app.models
django.setup()


class CourseTestCase(TestCase):
    def setUp(self):
        self.test_Ins = User.objects.create(username="testInsUser", name="testInsName", password="123",
                                            email="testIns@uwm.edu", role="Instructor", phone="123-456-7890",
                                            address="testInsAddress", officenumber="E252", officehoursStart="10:00",
                                            officehoursEnd="10:50", officehoursDays=[], skills="")
        self.test_TA_User = User.objects.create(username="testTAUser", name="testTAName", password="123",
                                                email="testTA@uwm.edu", role="TA", phone="123-456-7890",
                                                address="testTAAddress", officenumber="E253", officehoursStart="01:00",
                                                officehoursEnd="02:00", officehoursDays=[], skills="")
        self.test_course1 = Course.objects.create(courseid="361", name="Test Course 1", credits="3")
        self.test_TA_TA = TA.objects.create(user=self.test_TA_User, graderstatus=False, numlabs=0,
                                            course=self.test_course1,
                                            assignedlabs=0)
        self.test_section1 = Section.objects.create(course=self.test_course1, sectionid="201", type="Lecture",
                                                    scheduleStart="11:00", scheduleEnd="12:45", scheduleDays="T",
                                                    TA_assigned=None)

#   CREATE COURSE TESTS
    def test_courseIdexists(self):
        Course.objects.create(courseid="337",name="Systems Programming",credits="3")
        self.assertEqual(createCourse("337", "Software Engineering", "3"), "Course with that ID already exists")

    def test_courseCreated(self):
        b = Course.objects.get(courseid="361")
        self.assertEqual("Test Course 1", b.name)
        self.assertEqual("3", b.credits)

    def test_nocourseid(self):
        self.assertEqual(createCourse("", "Software Engineering", "3"), "Please fill out all required entries")

    def test_nocoursename(self):
        self.assertEqual(createCourse("361", "", "3"), "Please fill out all required entries")


    def test_nocoursecredits(self):
        self.assertEqual(createCourse("361", "Software Engineering", ""), "Please fill out all required entries")

#   DELETE COURSE TESTS
    def test_deletenocourseidentered(self):
        self.assertEqual(deleteCourse(""), "Please enter a course ID")

    def test_deletenocourseexists(self):
        self.assertEqual(deleteCourse("332"), "Course with that ID does not exist")

    def test_deletecourse(self):
        course1 = Course.objects.create(courseid="337",name="Systems Programming",credits="3")
        self.assertEqual(course1.courseid, "337")
        self.assertEqual(deleteCourse("337"), "Course with ID 337 has been deleted")

#   CREATE SECTION TESTS
    def test_createSection_badParam(self):
        self.assertEqual(createSection(None, "202", "Lecture", "11:00", "12:45", ["Tuesday"]),
                         "Please fill out all required entries")
        self.assertEqual(createSection(self.test_course1, None, "Lecture", "11:00", "12:45", ["Tuesday"]),
                         "Please fill out all required entries")
        self.assertEqual(createSection(self.test_course1, "202", None, "11:00", "12:45", ["Tuesday"]),
                         "Please fill out all required entries")
        self.assertEqual(createSection(self.test_course1, "202", "Lecture", None, "12:45", ["Tuesday"]),
                         "Please fill out all required entries")
        self.assertEqual(createSection(self.test_course1, "202", "Lecture", "11:00", None, ["Tuesday"]),
                         "Please fill out all required entries")
        self.assertEqual(createSection(self.test_course1, "202", "Lecture", "11:00", "12:45", None),
                         "Please fill out all required entries")
        self.assertEqual(createSection(self.test_course1, "202", "Lecture", "11:00", "12:45", []),
                         "Please fill out all required entries")

    def test_createSection_sectionExists(self):
        self.assertEqual(createSection(self.test_course1, "201", "Lecture", "11:00", "12:45", ["Tuesday"]),
                         "Section with that ID already exists")

    def test_createSection_goodParam(self):
        self.assertEqual(createSection(self.test_course1, "202", "Lecture", "11:00", "12:45", ["Tuesday"]), "")

#   DELETE SECTION TESTS
    def test_deleteSection_badParam(self):
        self.assertEqual(deleteSection(None), "Please enter a section ID")

    def test_deleteSection_sectionDNE(self):
        self.assertEqual(deleteSection("202"), "Section with that ID does not exist")

    def test_deleteSection_goodParam(self):
        self.assertEqual(deleteSection("201"), "Section with ID 201 has been deleted")

#   GET COURSES TESTS
    def test_getCourses_noCourses(self):
        deleteCourse("361")
        self.assertEqual(getCourses(), {})

    def test_getCourses_noLabs(self):
        deleteSection("201")
        self.assertEqual(getCourses(), {self.test_course1: []})

    def test_getCourses_success(self):
        self.assertEqual(getCourses(), {self.test_course1: [self.test_section1]})

#   ASSIGN INSTRUCTOR TO A COURSE
    def test_assignInstructor_badParam(self):
        self.assertEqual(assignInstructor(None, None), "Please select a course")
        self.assertEqual(assignInstructor("", ""), "Please select a course")
        self.assertEqual(assignInstructor(None, "testInsUser"), "Please select a course")
        self.assertEqual(assignInstructor("", "testInsUser"), "Please select a course")
        self.assertEqual(assignInstructor(self.test_course1, None), "Please select an instructor")
        self.assertEqual(assignInstructor(self.test_course1, ""), "Please select an instructor")

    def test_assignInstructor_goodParam(self):
        self.assertEqual(assignInstructor(self.test_course1, "testInsUser"), "")

#   ASSIGN TA TO A COURSE
    def test_assignTAtoCourse_badParam(self):
        self.assertEqual(assignTAtoCourse("", "", "", ""), "Please select a course")
        self.assertEqual(assignTAtoCourse(None, None, None, None), "Please select a course")

        self.assertEqual(assignTAtoCourse("", "testTAUser", 1, True), "Please select a course")
        self.assertEqual(assignTAtoCourse(None, "testTAUser", 1, True), "Please select a course")

        self.assertEqual(assignTAtoCourse(self.test_course1, "", 1, True), "Please select a TA")
        self.assertEqual(assignTAtoCourse(self.test_course1, None, 1, True), "Please select a TA")

        self.assertEqual(assignTAtoCourse(self.test_course1, "testTAUser", "", True), "Please enter the number of labs")
        self.assertEqual(assignTAtoCourse(self.test_course1, "testTAUser", None, True), "Please enter the number of labs")
        self.assertEqual(assignTAtoCourse(self.test_course1, "testTAUser", -1, True), "Please enter the number of labs")

    def test_assignTAtoCourse_goodParam(self):
        self.assertEqual(assignTAtoCourse(self.test_course1, "testTAUser", 1, True), "")

#   ASSIGN TA TO A SECTION TESTS
    def test_assignTAtoSection_badParam(self):
        self.assertEqual(assignTAtoSection("", ""), "Please select a section")
        self.assertEqual(assignTAtoSection(None, None), "Please select a section")
        self.assertEqual(assignTAtoSection("", "testTAUser"), "Please select a section")
        self.assertEqual(assignTAtoSection(None, "testTAUser"), "Please select a section")
        self.assertEqual(assignTAtoSection("201", ""), "Please select a TA")
        self.assertEqual(assignTAtoSection("201", None), "Please select a TA")

    def test_assignTAtoSection_goodParam(self):
        self.assertEqual(assignTAtoSection("201", "testTAUser"), "")

#   GET TAs IN SECTION TESTS
    def test_getTAsInCourse(self):
        assignTAtoSection("201", "testTAUser")
        with self.assertRaises(project_app.models.Section.DoesNotExist):
            getTAsInCourse("202")

#   UNASSIGN TA IN COURSE TESTS
    def test_unAssignTA(self):
        assignTAtoCourse(self.test_course1, "testTAUser")
        with self.assertRaises(project_app.models.User.DoesNotExist):
            unAssignTA("userNonexistent")
        with self.assertRaises(project_app.models.TA.DoesNotExist):
            unAssignTA("testInsUser")
        self.assertEqual(unAssignTA("testTAUser"), "testTAName has been unassigned from course with ID 361")

#   UNASSIGN TA IN SECTION TESTS
    def test_unAssignTASection(self):
        assignTAtoCourse(self.test_course1, "testTAUser")
        assignTAtoSection("201", "testTAUser")
        with self.assertRaises(project_app.models.Section.DoesNotExist):
            unAssignTASection("202")
        self.assertEqual(unAssignTASection("201"), "testTAName has been unassigned from section with ID 361-201")

#   UNASSIGN INSTRUCTOR
    def test_unAssignInstructor(self):
        assignInstructor(self.test_course1, "testInsUser")
        with self.assertRaises(project_app.models.Course.DoesNotExist):
            unAssignInstructor("362")
        self.assertEqual(unAssignInstructor("361"), "testInsName has been unassigned from course with ID 361")





