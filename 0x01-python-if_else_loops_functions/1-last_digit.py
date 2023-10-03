#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = int(str(number)[-1])
if number < 0:
    last_number = -last_number
string1 = f"Last digit of {number} is {last_number} "
if last_number == 0:
    string2 = "and is 0"
elif last_number > 5:
    string2 = "and is greater than 5"
else:
    string2 = "and is less than 6 and not 0"
print(string1 + string2)
