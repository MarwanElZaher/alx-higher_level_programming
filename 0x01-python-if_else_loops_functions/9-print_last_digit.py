#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    lastDigit = number % 10
    print("{}".format(lastDigit), end=(""))
    return lastDigit
