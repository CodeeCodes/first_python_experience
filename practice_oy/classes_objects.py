
# objects and classes
# create own data type that you want to use in Py

# modelling a student (create student data type)

# defining what the student is (has attributes inputted)
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = ""

    def is_on_honor_roll(self):
        if self.gpa >= 3.8:
            return True
        else:
            return False

