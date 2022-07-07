#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    solution = 0
    temp = 0
    for i in range(1, len(sys.argv)):
        number = int(sys.argv[i])
        number2 = number + temp
        solution = number
    print("{}".format(solution))
