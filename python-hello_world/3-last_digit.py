#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
print("Last digit of", number, "is", -last_digit if number < 0 else last_digit, end=" ")

if number > 5:
    print("and is greater than 5")

elif number < 6 and number != 0:
    print("and is less than 6 and not 0")

else:
    print("and is 0")

    
