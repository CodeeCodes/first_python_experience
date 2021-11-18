
secret_word = ""
response_user = ""
response_count = 0
response_limit = 3
out_of_guesses = False

secret_word = input("User One enter secret word: ")

while response_user != secret_word and not out_of_guesses:
    if response_count < response_limit:
        response_user = input("User Two enter the secret word: ")
        response_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print ("Try again")
else:
    print ("You win")
