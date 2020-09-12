#! /usr/bin/env python3

FIZZ = "Fizz"
BUZZ= "Buzz"

def fizzbuzz(value):
    """
    For each multiple of 3, print "Fizz" instead of the value.
    For each multiple of 5, print "Buzz" instead of the value.
    For numbers which are multiples of bothe 3 and 5, print "FizzBuzz" instead of the value.

    :params value: Input value
    :returns: Returns  "Fizz", "Buzz", "FizzBuzz", or string representation of the value.
    """
    try:
        if (value % 3 == 0) and (value % 5 == 0):
            return FIZZ + BUZZ
        elif (value % 3 == 0):
            return FIZZ
        elif (value % 5 == 0):
            return BUZZ
        else:
            return str(value)
    except Exception as e:
        print(f"{e!r}")
