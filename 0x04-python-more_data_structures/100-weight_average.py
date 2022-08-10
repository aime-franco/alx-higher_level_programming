#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for i in my_list:
        average += i[0] * tup[1]
        div += tup[1]
    return float(average / div)
