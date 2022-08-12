#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = a / b
    except (ValueError, ZeroDivisionError):
        return None
    finally:
        print("{}".format(quotient))
    return quotient
