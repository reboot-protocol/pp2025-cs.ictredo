class Course_info():
    def __init__(self,course_name,course_id):
        self.course_name = course_name
        self.course_id = course_id
    def __str__(self):
        return f"Course name: {self.course_name}, Course id : {self.course_id}"