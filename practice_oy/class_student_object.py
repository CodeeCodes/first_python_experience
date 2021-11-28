
# import class function from file

from classes_objects import Student

# create student object

student_1 = Student("Codee", "Computer Science", 4, False)
student_2 = Student("Astrid", "Performing Arts", 3.7, False)

# access objects by naming key value pair

print (student_1.gpa)
print (student_2.is_on_honor_roll())