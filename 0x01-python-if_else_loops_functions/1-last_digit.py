#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1
str1 = "Last digit of {} is {} ".format(number, last_digit)
if last_digit > 5:
    print(str1 + "and is greater than 5")
elif last_digit == 0:
    print(str1 + "and is 0")
else:
    print(str1 + "and is less than 6 and not 0")
