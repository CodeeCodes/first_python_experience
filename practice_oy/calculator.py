
#float has o be a number
num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter your second number: "))
operator = input("Enter your operator: ")


if operator == "+":
    print (num_1 + num_2)
elif operator == "-":
    print (num_1 - num_2)
elif operator == "*":
    print (num_1 * num_2)
elif operator == "/":
    print (num_1 / num_2)
else:
    print ("Incorrect input, try again")

