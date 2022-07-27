# . Create a Python project to guess a number that has randomly selected.
import random
print("       Welcome To The Guessing Game   \n")
random_number = random.randrange(0, 100)

tries = 5
while tries > 0:
    try:
        input_number = int(
            input("Try to guess the number :        \n"))

        tries -= 1
        if input_number > random_number:
            print("This is higher than the correct number, Try again \n", "*"*20)

        elif input_number < random_number:
            print(f"This is lower than the correct number, Try again  \n", "*"*20)

        else:
            print("That is correct YOU WIN !!\n")
            break
    except:
        print("Only Integers between 0,100 are Allowed \n",  "*"*20)
        tries -= 1
else:
    print("YOU LOSE!!\n")
    print(f"MY number was {random_number}")
stop = input("")
