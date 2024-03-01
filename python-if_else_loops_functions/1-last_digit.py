#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string_number = str(number)
last_digit = string_number[-1]
if int(last_digit) >5:
    print(f"The last digit of {number} is {last_digit} and is greater than 5")
elif int(last_digit) == 0:
    print(f"The last digit of {number} is {last_digit} and is 0")
elif int(last_digit) < 6 and int(last_digit) != 0:
    print(f"The last digit of {number} is {last_digit} and is less than 6 and not 0")
