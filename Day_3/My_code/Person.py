#%%
class Person(object):
    """docstrin for Person"""
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def person_name(cls, lastname, firstname):
        print(firstname + " " + lastname)
    # def getFirstname(self):
    #     return self.firstname
    # def getLastname(self):
    #     return self.lastname
    # def fullname(self):
    #     return "%s is a %s" % (self.firstname, self.lastname)
class Student(Person):
    def __init__(self, firstname, lastname, subject_area):
        super(Student, self). __init__(firstname, lastname)
        self.subject_area = subject_area

    @classmethod
    def student_name(cls, lastname, firstname, subject_area):
        print(firstname + " " + lastname + ", " + subject_area)

        
person = Person("Yrsa","Larsson")
Person.person_name(person.lastname, person.firstname)
student = Student("Yrsa", "Larsson", "PhD student")
Student.student_name(student.firstname, student.lastname, student.subject_area)

class Teacher(Person):
    def __init__(self, firstname, lastname, teaching_course):
        super(Teacher, self). __init__(firstname, lastname)
        self.teaching_course = teaching_course
    
    @classmethod
    def teacher_name(cls, firstname, lastname, teaching_course):
        print(firstname + " " + lastname + ", " + teaching_course)

teacher = Teacher("Adam","Sandler","Drama")
Teacher.teacher_name(teacher.firstname, teacher.lastname, teacher.teaching_course)

# %%
