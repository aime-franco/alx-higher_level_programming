#!/usr/bin/python3
def safe_print_integer(value):
    output = 0
    for i in value:
        try:
            print("{}".format(value))
            output += 1
            if value != str(value):
                return True
            else:
                return False
        except TypeError:
            break
    print()
    return output
