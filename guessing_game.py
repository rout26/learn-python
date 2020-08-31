import random
num = random.randint(1,10)
print("Guess a number between 1 and 10")

while 1:
    guessed_number = input()
    i= int(guessed_number)
    if i==num:
        print("You gueseed right!")
        print("===================")
    elif i<num:
        print("Try again..\nGuess higher===>")
    elif i>num:
        print("Try again..\nGuess lower===>")






