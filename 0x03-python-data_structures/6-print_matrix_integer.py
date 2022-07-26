#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for col in num:
            if num != col:
                print("{:d}".format(col), end=" ")
            else:
                print()
