#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for num in my_list:
        if num not in my_list:
            unique.append(num)
    return sum(unique)
