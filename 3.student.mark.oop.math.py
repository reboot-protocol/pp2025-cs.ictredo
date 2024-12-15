import numpy
import math
import curses
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

class Course_info():
    def __init__(self,course_name,course_id):
        self.course_name = course_name
        self.course_id = course_id
    def __str__(self):
        return f"Course name: {self.course_name}, Course id : {self.course_id}"
   

class Course_mark():
    def __init__(self,course_id,course_mark):
        self.course_id = course_id
        self.course_mark = course_mark
    def __str__(self):
        return f"Course id: {self.course_id} , Course mark :{self.course_mark} | "
def sort(student_list):
    for i in range(0,student_list.size):
        student_list[i].avg_gpa()
    temp_arr = numpy.argsort([student.gpa for student in student_list])
    return student_list[temp_arr]
def display(stdscr, Student_list, Course_list):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_CYAN,curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.curs_set(0)  
    stdscr.nodelay(0)  
    stdscr.clear()  
    row = 0

    stdscr.addstr(row, 0, "------------------------------------",curses.color_pair(1))
    stdscr.addstr(row + 1, 0, "Course Info:",curses.color_pair(3))
    row += 2
    for course in Course_list:
        stdscr.addstr(row, 0, str(course),curses.color_pair(4))
        row += 1
    stdscr.addstr(row, 0, "------------------------------------",curses.color_pair(1))
    row += 1

    Student_list = sort(Student_list)
    stdscr.addstr(row, 0, "Student List (sorted by GPA):",curses.color_pair(3))
    row += 1

    for student in Student_list:
        stdscr.addstr(row, 0, "------------------------------------",curses.color_pair(1))
        row += 1
        stdscr.addstr(row, 0, str(student),curses.color_pair(2))
        row += 1
        stdscr.addstr(row,0,str(student.print_mark()),curses.color_pair(2))
        row += 1
        gpa = student.avg_gpa()
        stdscr.addstr(row, 0, f"GPA: {gpa}",curses.color_pair(2))
        row += 1
        stdscr.addstr(row, 0, "------------------------------------",curses.color_pair(1))
        row += 1

    stdscr.getch()
    stdscr.refresh()




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
        if(Course_list.size == 0):
            Student_list = numpy.append(Student_list,Student(input("id "),input("name "),input("bod ")))
        elif(Course_list.size != 0):
            Student_list = numpy.append(Student_list,Student(input("id "),input("name "),input("bod ")))
            for i in range (0, Course_list.size):
                temp1 = math.floor(float(input(f"input mark for course id {Course_list[i].course_id} ")))
                temp2 = Course_list[i].course_id
                Student_list[Student_list.size-1].inputmark(temp1,temp2)
    elif(check == 2):
        if(Student_list.size == 0):
            Course_list = numpy.append(Course_list,Course_info(input("name: "),input("id: ")))
        elif(Student_list.size != 0):
            Course_list = numpy.append(Course_list,Course_info(input("name: "),input("id: ")))
            for i in range(0,Student_list.size):
                temp3 = math.floor(float(input(f"input mark for student with id {Student_list[i].id} ")))
                temp4 = Course_list[Course_list.size-1].course_id
                Student_list[i].inputmark(temp3,temp4)
    elif(check == 4):
      curses.wrapper(display,Student_list,Course_list) 
 
    elif(check == 3):
        break
    
        
"""
print("------------------------------------")
    print("Course info")
    for i in range(0,Course_list.size):
        print(Course_list[i])    
            
    print("------------------------------------")        
    Student_list = sort(Student_list)        
    print("Studen list (already sorted base on GPA in ascended )")        
    for i in range(0,Student_list.size):    
            print("------------------------------------")            
            print(Student_list[i])            
            Student_list[i].print_mark()            
            t = Student_list[i].avg_gpa()            
            print(f"GPA {t}")            
            print("------------------------------------")            
    print("------------------------------------")      
"""


