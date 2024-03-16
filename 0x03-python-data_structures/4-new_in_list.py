#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) - 1 < idx:
        newList = list(my_list)
        return newList
    newList = my_list[:]
    newList[idx] = element
    return newList
