#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = ["+", "-", "/", "*"]
    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[2])
    b = int(sys.argv[2])
    if sys.argv[2] == "+":
        print("{:d} {:d} = {:d}".format(a, sys.argv[2], b, add(a, b)))
    elif sys.argv[2] == "-":
        print("{:d} {:d} = {:d}".format(a, sys.argv[2], b, sub(a, b)))
    elif sys.argv[2] == "*":
        print("{:d} {:d} = {:d}".format(a, sys.argv[2], b, mul(a, b)))
    elif sys.argv[2] == "/":
        print("{:d} {:d} = {:d}".format(a, sys.argv[2], b, div(a, b)))
