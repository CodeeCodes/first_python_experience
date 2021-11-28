
# opening file in same directory
# open keyword get files (type out file)
# read/write/a(append) and r+(read and write) modes second parameter
employee_list = open("employee.txt", "r")

for employee in employee_list.readlines():
    print(employee)

# print (employee_list.readlines()[1])

# always close file
employee_list.close()

# writing and appending to files

employee_list = open("employee.txt", "a")

# escape character \n
employee_list.write("\nToby - Human Resources")

employee_list.close()

employee_list = open("employee_1.txt", "w")

# escape character \n
employee_list.write("\nNew file of employees")

employee_list.close()
