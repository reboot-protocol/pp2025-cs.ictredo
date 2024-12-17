import math
import numpy
import zipfile
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
        with open("student.txt", 'r') as fp:
            lines = len(fp.readlines())/3
            fp.close()
        f = open("student.txt","r")
        for i in range(0,int(lines)):
            id = f.readline().strip()
            name = f.readline().strip()
            bod = f.readline().strip()
            Student_list= numpy.append(Student_list,Student(id,name,bod))
        f.close()
    except:
        print("no student save file detected") 


    try:
        with open("course.txt", 'r') as fp:
            lines = len(fp.readlines())/2
            fp.close()
        f = open("course.txt","r")
        for i in range(0,int(lines)):
                name = f.readline().strip()
                id = f.readline().strip()
                Course_list = numpy.append(Course_list,Course_info(name,id))
        f.close()
    except Exception:
        print("no course save file detected") 

    try:
        Std_lines = Student_list.size
        mark_lines = Course_list.size
        f = open("mark.txt","r")
        for student in Student_list:
                temp0 = f.readline().strip()
                if(student.id == temp0):
                    for i in range(0,mark_lines):
                        id = f.readline().strip()
                        mark = math.floor(float(f.readline().strip()))
                        student.inputmark(mark,id)
                else: 
                    continue
        f.close()


    except Exception:
        print("no mark save file detected")
    return [Student_list,Course_list]
def decompress_save():
    try:
        with ZipFile("student.dat.zip","r") as zip:
            zip.extractall()
            zip.close()
    except Exception:
         print("no file save exist")
    