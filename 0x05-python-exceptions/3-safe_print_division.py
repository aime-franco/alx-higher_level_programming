#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = int(a) / int (b)
        return quotient
    except (ValueError, ZeroDivisionError):
        return None
    finally:
        print("{}".format(quotient))
    return quotient
