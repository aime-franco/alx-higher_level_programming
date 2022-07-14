#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numbers = 0
    for num in range(1, len(argv)):
        numbers += argv[num]
    print("{}".format(numbers))
