import curses
import numpy
import math

from domains import course as Course_info
from domains.student import Student,Course_mark,sort
from output import display
from input import inp_course, inp_student
check = 0
Student_list = numpy.array([])
Course_list =numpy.array([])
intro = """Press 
1 for : add student
2 for : add course
3 for : exit
4 for : print all info"""                                                
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
 
    elif(check == 3):
        break
