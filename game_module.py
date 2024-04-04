import sys
import random

#help(random)
#print(dir(random))

while True:
    #user_number = int(input("Guess a number between 1 and 5? "))
    user_number = sys.argv[1]
    random_number = (random.choice([1,2,3,4,5]))
    if user_number == random_number:
        print("you are a winner?")
        break
    else:
        print("try again")
        continue
    break
