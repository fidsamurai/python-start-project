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
    print("Character types do not add up to the total specified")
    exit()

char_num_list = (
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", upper),
    ("abcdefghijklmnopqrstuvwxyz", lower),
    ("0123456789", digit),
    (";:<>?/|[]{}_-+=()*&^%$#@!", special),
)
pass_list = []
for characters, number in char_num_list:
    picked_list = random.choices(characters, k=number)
    pass_list.extend(picked_list)

random.shuffle(pass_list)
password = "".join(pass_list)
print(password)
