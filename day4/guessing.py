i = 1
secret = 8
guess_limit = 3

while i <= guess_limit:
    guess = input("Guess the number: ")
    if int(guess) == secret:
        print("you Win!")
        exit()
    i = i + 1

print("You Failed!")