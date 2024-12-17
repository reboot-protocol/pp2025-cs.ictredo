import numpy

class Student():
    def __init__(self,id,name,bod):
        self.id = id
        self.name = name
        self.bod = bod
        self.Studentmark =numpy.array([])
    def __str__(self):
        return f"Student id: {self.id}, Student name: {self.name}, Student bod :{self.bod}"
    def inputmark(self,mark,id):
        self.Studentmark = numpy.append(self.Studentmark,Course_mark(id,mark))
    def print_mark(self):
        t =""
        for m in self.Studentmark:
            t = t + str(m)
        return t
    def avg_gpa(self):
        temp = numpy.array([course.course_mark for course in self.Studentmark])
        avg = numpy.average([temp])
        self.gpa = avg
        return avg
class Course_mark():
    def __init__(self,course_id,course_mark):
        self.course_id = course_id
        self.course_mark = course_mark
    def __str__(self):
        return f"Course id: {self.course_id} , Course mark :{self.course_mark} | "
def sort(student_list):
    for student in student_list:
        student.avg_gpa()
    temp_arr = numpy.argsort([student.gpa for student in student_list])
    return student_list[temp_arr] 