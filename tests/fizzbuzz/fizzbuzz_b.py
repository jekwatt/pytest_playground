#! /usr/bin/env python3

FIZZ = "Fizz"
BUZZ = "Buzz"

def fizzbuzz_b(value):
    return (FIZZ * (value % 3 == 0) + BUZZ * (value % 5 == 0) or str(value))
