import re
class Student:
    validdegrees = ["ECE", "BIO", "MECH", "EEE"]

    def __init__(self, name, degree, StudentID):
        global validdegrees
        if name!= "":
            self.name = name
        else:
            print("You have to have a name")
            raise NameError
        
        for degrees in self.validdegrees:
            if degree == degrees:
                self.degree = degree

        if re.search("[0-9]{6}", StudentID):
            self.StudentID = StudentID
        else:
            print("Invalid ID")
    
    @property
    def getdegree(self):
        return self.degree
    
    @degree.setter
    def degree(self,degree):
        self.degree = degree
    
    def getstudent(self):
        print(self.name)
        print(self.degree)
        print(self.StudentID)

class Course:
    def __init__(self,coursename,coursecode):
        self.coursename = coursename
        self.coursecode = coursecode

    @property
    def getcoursename(self):
        return self.coursename
    @property
    def getcoursecode(self):
        return self.coursecode

    @coursename.setter
    def coursename(self, course):
        self.coursename = course
    
    @coursecode.setter
    def coursecode(self, code):
        self.coursecode = code

student = Student("Josh","MECH","123456")
student.getstudent()
print(student.getdegree)

