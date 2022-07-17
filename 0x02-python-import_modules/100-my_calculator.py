#!/usr/bin/python3
if __name__ == "__main__":
    from calculator import add, sub, mul, div
    from sys import argv
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
    if args[2] != "+" and args != "*" and args != "/" and args != "-":
        print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
    a = int(args[1])
    b = int(args[3])
    if args[2] == "+":
        print("{:d} {:d} = {:d}".format(a,args[2], b, add(a, b)))
    elif args[2] == "-":
        print("{:d} {:d} = {:d}".format(a, args[2], b, sub(a, b)))
    elif args[2] == "*":
        print("{:d} {:d} = {:d}".format(a, args[2], b, mul(a, b)))
    elif args[2] == "/":
        print("{:d} {:d} = {:d}".format(a, args[2], b, div(a, b)))
