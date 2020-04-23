#!/usr/bin/env python3.7

import random

total_char = int(input("Total characters: "))

if total_char < 6:
    print("Minimum character length is 6")
    exit()

upper = int(input("How many Upper case characters?: "))
if upper < 1:
    print("There has to be one Upper Case Character!")
    exit()
lower = int(input("How many Lower case characters?: "))
if lower < 1:
    print("There has to be one Lower Case Character!")
    exit()
digit = int(input("How many digits?: "))
if digit < 1:
    print("There has to be one digit!")
    exit()
special = int(input("How many Special characters?: "))
if special < 1:
    print("There has to be one Special Character!")
    exit()

if total_char != upper + lower + digit + special:
    print("Characters do not add up!")
    exit()

pass_list = []

upper_list = random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k = upper)
pass_list.extend(upper_list)

lower_list = random.choices("abcdefghijklmnopqrstuvwxyz", k = lower)
pass_list.extend(lower_list)

digit_list = random.choices("0123456789", k = digit)
pass_list.extend(digit_list)

special_list = random.choices("!@#$%^&*()-_+|<>/?,.:;", k = special)
pass_list.extend(special_list)

random.shuffle(pass_list)
password = "".join(pass_list)
print(password)
