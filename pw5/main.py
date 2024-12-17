import curses
import numpy
import math
from domains.course import Course_info
from domains.student import Student,Course_mark,sort
from output import display,save_exp,compress_save
from input import inp_course, inp_student,save_imp,decompress_save
check = 0
Student_list = numpy.array([])
Course_list =numpy.array([])
intro = """Press 
1 for : add student
2 for : add course
3 for : exit and no save
4 for : print all info
5 for : exit and save """ 
decompress_save()
li_ca = []
li_ca = save_imp(Student_list,Course_list)
Student_list = li_ca[0]
Course_list = li_ca[1]
while (check != 3):
    print(intro)
    check = int(input())
    
    
    if(check == 1):
        Student_list = inp_student(Student_list,Course_list)
    elif(check == 2):
        
        temp_list  = inp_course(Student_list,Course_list)
        Student_list = temp_list[0]
        Course_list = temp_list[1]
    elif(check == 4):
      curses.wrapper(display,Student_list,Course_list) 
      #for student in Student_list:
          #print(student.avg_gpa()) 
    elif(check == 3):
        break
    elif(check == 5):
        save_exp(Student_list,Course_list)
        compress_save()


        break
