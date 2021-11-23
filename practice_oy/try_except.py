

# try/except block
try:
    answer = 10/0
    number = float(input("Enter a number: "))
    print(number)
# always use specific error 
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print ("invalid input")

