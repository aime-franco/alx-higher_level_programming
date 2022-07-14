#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{} argument".format(len(argv) - 1), end="")
    if len(argv) == 0:
        print("argument.")
    elif args > 1:
        if args == 1:
            print("argument:")
        elif args > 2:
            print("arguments:")
        for i in range(args -1):
            print("{}: {}".format((i + 1), sys.argv[i + 1]))
