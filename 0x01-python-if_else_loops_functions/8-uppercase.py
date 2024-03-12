#!/usr/bin/python3
def uppercase(str):
   if str >= ord("97") or str <= ord("122"):
     print("{:c}".format(str - 32), end="")