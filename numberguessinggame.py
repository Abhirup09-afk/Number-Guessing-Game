#program a number guessing game

import random

print("Welcome to the number guessing game. This is a python project made by Abhirup Mitra.")
num = random.randint(1, 100)
crt = 0
trl = 4

while crt < 5:
    guess = int(input("Enter your guess number in range from 1 to 100: "))

    if guess == num:
        print("Your guess is actually correct. Therefore you WIN!")
        print("The actual number was: ", num)

        break

    else: 
        if abs(num - guess) <= 10:
            print("You are really close to the number! you are ", abs(num - guess), "point(s) far from it \n""You have only,", trl, "chances left...")

        else:
            print("You are really far from the number. Try again! ""You have only,", trl, "chances left...")

        crt += 1
        trl -= 1

if not crt < 5:
    print("Sorry to say that you have lost all your chances and thus you LOSE :( \n Try again next time.")
    print("The actual number was: ", num)
