class Student():
    def __init__(self,id,name,bod):
        self.id = id
        self.name = name
        self.bod = bod
        self.Studentmark =[]
    def __str__(self):
        return f"Student id: {self.id}, Student name: {self.name}, Student bod :{self.bod}"
    def inputmark(self,mark,id):
        self.Studentmark.append(Course_mark(id,mark))
    def print_mark(self):
        for i in range(0,len(self.Studentmark)):
            print(self.Studentmark[i])
        

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
        return f"Course id: {self.course_id} , Course mark :{self.course_mark}"



check = 0
Student_list = []
Course_list =[]
intro = """Press 
1 for : add student
2 for : add course
3 for : exit
4 for : print all info"""                                                
while (check != 3):
    print(intro)
    check = int(input())
    
    
    if(check == 1):
        if(len(Course_list) == 0):
            Student_list.append(Student(input("id "),input("name "),input("bod ")))
        elif(len(Course_list) != 0):
            Student_list.append(Student(input("id "),input("name "),input("bod ")))
            for i in range (0, len(Course_list)):
                temp1 = input(f"input mark for course id {Course_list[i].course_id} ")
                temp2 = Course_list[i].course_id
                Student_list[len(Student_list)-1].inputmark(temp1,temp2)
    elif(check == 2):
        if(len(Student_list) == 0):
            Course_list.append(Course_info(input("name: "),input("id: ")))
        elif(len(Student_list) != 0):
            Course_list.append(Course_info(input("name: "),input("id: ")))
            for i in range(0,len(Student_list)):
                temp3 = input(f"input mark for student with id {Student_list[i].id} ")
                temp4 = Course_list[len(Course_list)-1].course_id
                Student_list[i].inputmark(temp3,temp4)
    elif(check == 4):
        print("------------------------------------")
        print("Course info")
        for i in range(0,len(Course_list)):
            print(Course_list[i])
        
        print("------------------------------------")
        
        print("------------------------------------")
        for i in range(0,len(Student_list)):
            print("------------------------------------")
            print(Student_list[i])
            Student_list[i].print_mark()
            print("------------------------------------")
        print("------------------------------------")
 
    elif(check == 3):
        break
    
        
    




