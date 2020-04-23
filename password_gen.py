#!/usr/bin/env python3.7

#Password Generator

import random
import string

length = int(input("Input length of password:"))
if length >= 6:
    pass
else:
    print("Please enter a character length above 6")
    exit()

num_lower = int(input("Number of lowercase letters:"))
num_upper = int(input("Number of UpperCase Letters:"))
num_num = int(input("Number of numbers:"))

def randPass():
        randSrc = string.ascii_letters + string.digits + string.punctuation
        password = random.choice(string.ascii_lowercase(num_lower))
        password += random.choice(string.ascii_uppercase(num_upper))
        password += random.choice(string.digits(num_num))
        password += random.choice(string.punctuation)

        for i in len(length):
            password += random.choice(randSrc)

        passwordList = list(password)
        random.SystemRandom() .shuffle(passwordList)
        password = ' '.join(passwordList)
        return password

print ("Random Password is ", randPass())
