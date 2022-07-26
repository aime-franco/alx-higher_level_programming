#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for col in num:
            print("{:d}".format(col), end=" " if col != row[-1]  else "")
        print()
