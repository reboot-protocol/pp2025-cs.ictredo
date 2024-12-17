import math
import numpy
import zipfile
import pickle
from zipfile import ZipFile
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


def save_imp(Student_list,Course_list):
    try:
        f = open("student.pickle","rb")
        sleng = pickle.load(f)
        for i in range(0,sleng):
             Student_list = numpy.append(Student_list,pickle.load(f))
        f.close()
    except Exception:
        print("no student && mark save file detected")
    try:
        f = open("course.pickle","rb")
        cleng = pickle.load(f)
        for i in range(0,sleng):
            Course_list = numpy.append(Course_list,pickle.load(f))
        f.close()
    except Exception:
        print("no course save file detected")
    return [Student_list,Course_list]


def decompress_save():
    try:
        with ZipFile("student.dat.zip","r") as zip:
            zip.extractall()
            zip.close()
    except Exception:
         print("no file save exist")
    