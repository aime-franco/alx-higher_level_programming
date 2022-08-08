#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    product = {}
    for key, i in a_dictionary.items():
        product[key] = i * 2
        
    return product
