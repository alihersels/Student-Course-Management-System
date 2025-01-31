class Student:
    def __init__(self, stdName, stdID, stdAttendance):
        self.stdName = stdName
        self.stdID = stdID
        self.stdAttendance = stdAttendance


class Course:
    def __init__(self, courseName):
        self.courseName = courseName


class Grade:
    def __init__(self, grade):
        self.grade = grade


class Report:
    def __init__(self, course, student, grade):
        self.course = course.courseName
        self.stdName = student.stdName
        self.stdID = student.stdID
        self.stdAttendance = student.stdAttendance
        self.grade = grade.grade
        if float(self.grade) < 50:
            self.verdict = "Needs Work"
        else:
            self.verdict = "Doesn't need Work"



    def report_generator(self):
        output = (self.course + " | " + self.stdName + " (" + self.stdID + ") | Grade Accumulation: " + self.grade +
                  " | Attendance: " + self.stdAttendance + " | Verdict: " + self.verdict)
        return output
