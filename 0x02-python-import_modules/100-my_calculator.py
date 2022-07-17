#!/usr/bin/python3
if __name__ == "__main__":
    from calculator import add, sub, mul, div
    import sys
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
    opps = {"*":mul, "-":add, "+":add, "/":div}
    if sys.argv[2] not in list(opps.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{} {} = {}".format(a,sys.argv[2], b, add(a, b)))
    elif sys.argv[2] == "-":
        print("{} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
    elif sys.argv[2] == "*":
        print("{} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
    elif sys.argv[2] == "/":
        print("{} {} = {}".format(a, sys.argv[2], b, div(a, b)))
