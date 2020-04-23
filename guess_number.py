#!/usr/bin/env python3.7

#Guess the Number Game

import random

rand = random.randrange(1, 10)
ans = int(input("Guess the machine generated number between 1-10:"))
if rand == ans:
    print("Hooray you guessed right!")
elif rand >= ans:
    print("Sorry try again, the answer was greater than what you guessed", rand )
else:
    print("Sorry try again, the answer was less than what you guessed", rand)
