#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_number = len(argv)
    addition = 0
    for i in range(1, args_number):
        addition += int(argv[i])
    print("{}".format(addition))
