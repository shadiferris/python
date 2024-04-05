from random import randint
import sys

first = int(sys.argv[1])

last = int(sys.argv[2])

answer = randint(first, last)



while True:
    try:
        print(answer)
        guess = int(input(f"Guess a number between {first} and {last} "))
        if first < guess < last:
          #print("things are working")
          if answer == guess:
            print("you successfully guessed the number.. well done")
            break
          else:
            print("number was incorrect, please select another number")
            continue
        else:
           print("number outside range, please select another number")
           continue
    except ValueError:
        print("please enter a number")
        continue
