from math import *
import useful_tools_python

# variables & strings
character_name = "Codee"
print(character_name + " Is High")
phrase = "High Dive"
print(character_name + " Goes to " + phrase)
print(phrase.lower())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())

# find position in string/grab character in string
print(phrase[6])

# find where word is indexed
print(phrase.index("Dive"))

# replace word in string
print(phrase.replace("Dive", "Donkey"))

# working with numbers
print(2 + 2 == (2 * 1 + 2 * 1))

# mod how many times it goes in
print(10 % 3)
print(3 % 10)

# variables
my_num_2 = -26
my_num = 26
print(my_num)

# absolute number *just the number
print(abs(my_num_2))

# numbers to the power of eg. 4*4 for this example
print(pow(2, 4))
print(pow(2, 5))

# round function
print(round(5, 10))

# math functions

print(floor(3))
print(ceil(3))
print(sqrt(4))

# imported module

print (useful_tools_python.feet_in_mile * 6.2)
