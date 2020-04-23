#!/usr/bin/env python3.7

#Password Generator Attempt 2
import random

characters = int(input("How many characters would you like?:"))

if characters >= 6:
    pass
else:
    print("Minimum charachter length is 6")
    exit()

upper = int(input("How many upper case characters?:"))
lower = int(input("How many lower case characters?:"))
digits = int(input("How many digits?:"))
spec_characters = int(input("How many Special Characters?:"))

tot_char = int(upper) + int(lower) + int(digits) +int(spec_characters)
if  tot_char == characters and int(upper) >= 1 and int(lower) >= 1 and int(digits) >= 1 and int(spec_characters) >= 1:
    pass
else:
    print("The total number of characters does not match what you had selected or one of the character types is set to 0")
    exit()

#upper_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#lower_list = ['a','b','c','d','e','f','g,','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#digit_list = [1,2,3,4,5,6,7,8,9,0]
#spec_characters_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', '<', '>', '?', '|', '/']

pass_list = []

for u in range(upper):
    upper_pass = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    pass_list.append(upper_pass)
for l in range(lower):
    lower_pass = random.choice("abcdefghijklmnopqrstuvwxyz")
    pass_list.append(lower_pass)
for d in range(digits):
    digit_pass = random.choice("0123456789")
    pass_list.append(digit_pass)
for s in range(spec_characters):
    spec_characters_pass = random.choice("!@:;#$%^&*,<>?|/")
    pass_list.append(spec_characters_pass)

random.shuffle(pass_list)
password = "".join(pass_list)
#print(upper_pass, lower_pass, digit_pass, spec_characters_pass)
print("Your random password is:", password)
