import zipfile
import numpy
import curses
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
            f = open("student.txt","w")
            for student in Student_list:
                f.write(f"{student.id}\n")
                f.write(f"{student.name}\n")
                f.write(f"{student.bod}\n")
            f.close()
        except Exception:
            
            f = open("student.txt","a")
            for student in Student_list:
                f.write(f"{student.id}\n")
                f.write(f"{student.name}\n")
                f.write(f"{student.bod}\n")
            f.close()

        try:
            f = open("course.txt","w")
            for course in Course_list:
                f.write(f"{course.course_name}\n")
                f.write(f"{course.course_id}\n")
            f.close()

        except Exception:
            f = open("course.txt","a")
            for course in Course_list:
                f.write(f"{course.course_name}\n")
                f.write(f"{course.course_id}\n")
            f.close()
        
        try:
            f = open("mark.txt","w")
            for student in Student_list:
                f.write(f"{student.id}\n")
                for mark in student.Studentmark:
                    f.write(f"{mark.course_id}\n")
                    f.write(f"{mark.course_mark}\n")
            f.close()
        except Exception:
            f = open("mark.txt","a")
            for student in Student_list:
                f.write(f"{student.id}\n")
                for mark in student.Studentmark:
                    f.write(f"{mark.course_id}\n")
                    f.write(f"{mark.course_mark}\n")
            f.close()
def compress_save():
    try:
        with ZipFile("student.dat.zip","w",zipfile.ZIP_STORED) as com:
            com.write("student.txt","student.txt")
            com.write("course.txt","course.txt")
            com.write("mark.txt","mark.txt")
            #zipf.setpassword(b"bestsecuritypasswordthateverexisted")
            com.close()
    except zipfile.error:
         print("error")           