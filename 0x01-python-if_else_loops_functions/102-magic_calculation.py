#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    else:
        if c > b:
            return a
    return (a * b) - c
