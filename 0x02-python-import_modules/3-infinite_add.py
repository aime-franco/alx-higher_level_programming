#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args_number = len(argv)
    addition = 0
    for i in range(1, args_number):
        addition += int(argv[i])
    print("{}".format(addition))
