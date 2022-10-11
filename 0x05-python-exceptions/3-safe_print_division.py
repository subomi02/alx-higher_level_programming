#!/usr/bin/python3
# 3-safe_print_division.py


def safe_print_division(a, b):
    """return a/b."""
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
