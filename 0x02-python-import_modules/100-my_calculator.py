#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sysargv) -1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, *, /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{:d} {:d} = {:d}".format(a, sys.argv[2],b, ops[sys.argv[2]](a, b)))
    from sys import argv
    from calculator_1 import add, sub, mul, div
    count = len(argv)
    if count != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    num1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]
    def not_found():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    def my_add():
        total = add(num1, num2)
        print("{:d} + {:d} = {:d}".format(num1, num2, total))
        return total
    def my_sub():
        total = sub(num1, num2)
        print("{:d} - {:d} = {:d}".format(num1, num2, total))
        return total
    def my_mul():
        total = mul(num1, num2)
        print("{:d} * {:d} = {:d}".format(num1, num2, total))
        return total
    def my_div():
        total = div(num1, num2)
        print("{:d} / {:d} = {:d}".format(num1, num2, total))
        return total
    options = {
        "+": my_add,
        "-": my_sub,
        "*": my_mul,
        "/": my_div
    }
    options.get(op, not_found)()
