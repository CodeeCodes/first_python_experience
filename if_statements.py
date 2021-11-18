
#if statements
is_female = True
is_male = False
is_tall = True

if is_male and is_tall:
    print ("you are a tall male")
elif is_male and not is_tall:
    print ("you are a short male")
elif is_female and is_tall:
    print ("you are a tall female")
else:
    print ("You are short female")


