import zipfile
import numpy
import curses
import pickle
from zipfile import ZipFile
from domains.student import Student,Course_mark,sort
from domains.course import Course_info
def display(stdscr, Student_list, Course_list):
    try:
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        
        curses.curs_set(0)  
        stdscr.nodelay(0)  
        stdscr.clear()  
        row = 0

        stdscr.addstr(row, 0, "------------------------------------", curses.color_pair(1))
        stdscr.addstr(row + 1, 0, "Course Info:", curses.color_pair(3))
        row += 2
        for course in Course_list:
            stdscr.addstr(row, 0, str(course), curses.color_pair(4))
            row += 1
        stdscr.addstr(row, 0, "------------------------------------", curses.color_pair(1))
        row += 1

        
        Student_list = sort(Student_list)
        stdscr.addstr(row, 0, "Student List (sorted by GPA):", curses.color_pair(3))
        row += 1

        for student in Student_list:
            stdscr.addstr(row, 0, "------------------------------------", curses.color_pair(1))
            row += 1
            stdscr.addstr(row, 0, str(student), curses.color_pair(2))
            row += 1
            stdscr.addstr(row, 0, str(student.print_mark()), curses.color_pair(2))
            row += 1
            gpa = student.avg_gpa()
            stdscr.addstr(row, 0, f"GPA: {gpa}", curses.color_pair(2))  
            row += 1
            stdscr.addstr(row, 0, "------------------------------------", curses.color_pair(1))
            row += 1

        stdscr.refresh()
        stdscr.getch()  
    except Exception:
        print("yout terminal/windows/vscode terminal screen too small, pls expand and choose option 5 then run it again")


def save_exp(Student_list,Course_list):
        try:
            f = open("student.pickle","bw")
            std_leng = len(Student_list)
            pickle.dump(std_leng,f)
            for student in Student_list:
                pickle.dump(student,f)
            f.close()
            
        except Exception:
            
            f = open("student.txt","ab")
            std_leng = len(Student_list)
            pickle.dump(std_leng,f)
            for student in Student_list:
                pickle.dump(student,f)
            f.close()
        

        try:
            f = open("course.pickle","wb")
            cou_leng = len(Course_list)
            pickle.dump(cou_leng,f)
            for course in Course_list:
                pickle.dump(course,f)
            f.close()

        except Exception:
            f = open("course.pickle","ab")
            cou_leng = len(Course_list)
            pickle.dump(cou_leng,f)
            for course in Course_list:
                pickle.dump(course,f)
            f.close()
        


def compress_save():
    try:
        with ZipFile("student.dat.zip","w",zipfile.ZIP_STORED) as com:
            com.write("student.pickle","student.pickle")
            com.write("course.pickle","course.pickle")
            com.close()
    except zipfile.error:
         print("error")           