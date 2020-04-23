#!/usr/bin/env python3.7

#Rock paper scissors

import random

rps = ['rock', 'paper', 'scissor']
cp = random.choice(rps)
human = input("Enter rock paper or scissor:")

if cp == human:
    print("You drew with the comp! ", cp)
elif cp == "rock" and human == "paper":
    print("You win, paper beats rock, ", cp)
elif cp == "paper" and human == "rock":
    print("Sorry, you lost, paper beats rock, ", cp)
elif cp == "scissor" and human == "rock":
    print("You win, rock beats scissor, ", cp)
elif cp == "rock" and human == "scissor":
    print("Sorry, you lost, rock beats scissor, ", cp)
elif cp == "paper" and human == "scissor":
    print("You win, scissor beats paper, ", cp)
elif cp == "scissor" and human == "paper":
    print("Sorry, you lost, scissor beats paper,    ", cp)
else:
    print("Please enter rock, paper or scissor")
