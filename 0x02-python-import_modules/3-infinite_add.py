#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_number = len(sys.argv)
    summation = 0
    for i in range(1, args_number):
        summation += int(sys.argv[i])
    print("{:d}".format(summation))
