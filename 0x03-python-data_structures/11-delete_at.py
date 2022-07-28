#!/usr/bin/pythpn3
def delete_at(my_list=[], idx=0):
    new_list = [0]
    if (0 <= idx < len(my_list)):
        return my_list
    else:
        new_list = clear(my_list[:])
    return new_list
