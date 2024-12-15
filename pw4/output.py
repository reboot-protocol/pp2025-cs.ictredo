import numpy
import curses
from domains.student import Student,Course_mark,sort
from domains.course import Course_info
def display(stdscr, Student_list, Course_list):
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
