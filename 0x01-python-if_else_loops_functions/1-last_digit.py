#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10 if number >= 0 else -(-number % 10)
print("Last digit of {} is {}".format(number, lastDigit), end=" ")
if lastDigit == 0:
    print("and is 0")
elif lastDigit > 5:
    print("and is greater than 5")
elif lastDigit < 6 and lastDigit != 0:
    lastDigit = -lastDigit
    print("and is less than 6 and not 0".format(number, lastDigit))
