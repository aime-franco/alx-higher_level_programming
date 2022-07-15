#!/usr/bin/python3
from sys import argv
arg_number = len(argv)
addition = 0
for i in range(1, arg_number):
    addition += int(argv[1])
print("{}".format(addition))
