#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            uppercase_char = chr(ord(char) - 32)
            print("{}".format(uppercase_char), end=(""))
    print("")
