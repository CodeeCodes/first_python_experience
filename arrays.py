# Arrays
peopleList = ["john", "elliot", "sarah", "codee", "astrid"]


print(peopleList[0])

# manipulating lists
peopleList[0] = "silver"

print(peopleList[0], peopleList[1])

print(peopleList[:2])

print(peopleList[2:])

print(peopleList[-1])

# Array functions

lucky_Numbers = [1, 3, 5, 7, 9, 13, 14, 18, 22]
friends = ["sam", "joe", "jamie", "cody", "liam"]

# push to list/array
friends.extend(lucky_Numbers)

# append to end of array
friends.append("astrid")

# insert to middle of array
friends.insert(3, "alex")

# remove from list
friends.remove("cody")

# remove last element from array
friends.pop()

# find element in list index
print(friends.index("jamie"))

print (friends)

# sort list ascending order
friends.sort()

print (friends)
