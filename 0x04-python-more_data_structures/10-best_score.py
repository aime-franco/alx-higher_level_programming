#!/usr/bin/python3
def best_score(a_dictionary):
    for i in a_dictionary:
        if i not in a_dictionary:
            return None
    new_value = {}
    new_value = max(a_dictionary, key=a_dictionary.get)
    return new_value
