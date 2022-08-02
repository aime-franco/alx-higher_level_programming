#!/usr/bin/python3
def print_sorted_dicitionary(a_dictionary):
    new_string = []
    for item in a_dictionary:
        new_string.append(item)
    new_string.sort()
    for i in new_string:
        print("{}: {}".format(i,  a_dictionary[i])
