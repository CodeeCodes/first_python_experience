
# translate word by replacing vowel with g

def translator_g(base_phrase):
    translation = ""
    for letter in base_phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print (translator_g(input("Enter a phrase here: ")))

