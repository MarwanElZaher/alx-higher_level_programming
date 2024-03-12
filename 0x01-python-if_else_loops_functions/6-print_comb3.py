#!/usr/bin/python3
for firstDigit in range(0, 9):
    for secondDigit in range(1, 10):
        print("{}{}".format(firstDigit, secondDigit), end=(", "))
        if(firstDigit % 10 == 9):
            print("{ + 2}".format(secondDigit), end=(", "))
