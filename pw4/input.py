import math
import numpy
from domains.student import Student,Course_mark
from domains.course import Course_info
def inp_student(Student_list,Course_list):
    if(Course_list.size == 0):
            Student_list = numpy.append(Student_list,Student(input("id "),input("name "),input("bod ")))
            return Student_list
    elif(Course_list.size != 0):
            Student_list = numpy.append(Student_list,Student(input("id "),input("name "),input("bod ")))
            for i in range (0, Course_list.size):
                temp1 = math.floor(float(input(f"input mark for course id {Course_list[i].course_id} ")))
                temp2 = Course_list[i].course_id
                Student_list[Student_list.size-1].inputmark(temp1,temp2)
            return Student_list    
def inp_course(Student_list,Course_list):
      if(Student_list.size == 0):
            Course_list = numpy.append(Course_list,Course_info(input("name: "),input("id: ")))
            return [Student_list,Course_list]
      elif(Student_list.size != 0):
            Course_list = numpy.append(Course_list,Course_info(input("name: "),input("id: ")))
            for student in Student_list:
                temp3 = math.floor(float(input(f"input mark for student with id {student.id} ")))
                temp4 = Course_list[Course_list.size-1].course_id
                student.inputmark(temp3,temp4)  
            return [Student_list,Course_list]