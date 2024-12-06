#Studenlist stid name bod
#courseinfo course_name course_id
#Coursemark stid course_mark course_id

def dumpdata_forstudent(Studentlist,a):
    for i in range(0,a):
        print(f"enter in sequence id name and bod for the no #{i+1}" )
        id_temp = input('id: ')
        name_temp = input('name: ')
        bod_temp = input('bod: ')
        Studentlist.append({"stid": id_temp,"name":name_temp,"bod":bod_temp})
def showinfo(student,cinfo,cmark):
    for i in range(0,len(student)):
        print("---------------------------------------")
        print(f"student id: {student[i]['stid']}")
        print(f"student name: {student[i]['name']}")
        print(f"student bod: {student[i]['bod']}")
        for j in range(0,len(cinfo)):
            print(f"course name: {cinfo[j]['course_name']},",end='')
            print(f" course id: {cinfo[j]['course_id']},",end='')
            for k in range(0,len(cmark)):
                if(student[i]["stid"] == cmark[k]["stid"] and cmark[k]["course_id"] == cinfo[j]["course_id"] ):
                    print(f" course mark:{cmark[k]['course_mark']}")
    print("---------------------------------------")
def dumpdata_courseinfo(Courseinfo,a):
    for i in range(0,a):
        print(f"enter in sequence id name and bod for the no #{i}" )
        coursename_temp = input('course name: ')
        courseid = input('course id: ')
        Courseinfo.append({"course_name": coursename_temp,"course_id":courseid})
def dumpdata_coursemark(Studentlist,Courseinfo,Coursemark):
    for i in range(0,len(Studentlist)):
        for j in range(0,len(Courseinfo)) :
            course_mark = input(f"enter the course mark for student ID {Studentlist[i]['stid']} in course {Courseinfo[j]['course_id']}: ")
            Coursemark.append({"course_id":Courseinfo[j]["course_id"],"stid": Studentlist[i]["stid"],"course_mark":course_mark})


         



#test
Student_list =[]
Course_info=[]
Course_mark =[]
print(" how many student?")
nst = int(input())
print("how many course?")
noc = int(input())
dumpdata_forstudent(Student_list,nst)
dumpdata_courseinfo(Course_info,noc)
dumpdata_coursemark(Student_list,Course_info,Course_mark)

showinfo(Student_list,Course_info,Course_mark)
""" debug 
Student_list = [
    {
        "stid" : "23bi1",
        "name" : "test1",
        "bod" : "1/1/2000"
    },
    {
        "stid" : "23bi2",
        "name" : "test2",
        "bod" : "1/1/2001"
    }
]
Course_info = [
    {
        "course_name" : "Physic",
        "course_id" : "Phy"
    },
    {
        "course_name" : "Calculus",
        "course_id" : "Mat"
    },
]
Course_mark = [
    {
        "course_id": "Phy",
        "stid" : "23bi1",
        "course_mark" : "10"
    },
    {
        "course_id": "Mat",
        "stid" : "23bi1",
        "course_mark" : "9"
    },
    {
        "course_id": "Phy",
        "stid" : "23bi2",
        "course_mark" : "8"
    },
    {
        "course_id": "Mat",
        "stid" : "23bi2",
        "course_mark" : "7"
    },
]
"""




    
    

