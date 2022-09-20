#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_dgt = int(repr(number)[-1])
if number < 0:
    last_dgt = last_dgt * -1
print("Last digit of", number, "is", last_dgt, end=" ")
if last_dgt > 5:
    print("and is greater than 5")
elif last_dgt == 0:
    print("and is 0")
elif last_dgt < 6 and not 0:
    print("and is less than 6 and not 0", end="\n")
