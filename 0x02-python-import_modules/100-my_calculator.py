#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops =("+", "-", "/", "*")
    if args[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(args[2])
    b = int(args[2])
    if args[2] == "+":
        print("{:d}  {:d} = { :d}".format(a, args[2], b, add(a, b)))
    elif args[2] == "-":
        print("{:d}  {:d} = { :d}".format(a, args[2], b, sub(a, b)))
    elif args[2] == "*":
        print("{:d}  {:d} = { :d}".format(a, args[2], b, mul(a, b)))
    elif args[2] == "/":
        print("{:d}  {:d} = { :d}".format(a, args[2], b, div(a, b)))
