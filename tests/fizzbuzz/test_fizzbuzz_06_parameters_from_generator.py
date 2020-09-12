# test_fizzbuzz_06_parameters_from_generator

import pytest

from fizzbuzz import fizzbuzz


def fizzbuzz_cases():
    for f in [
        (3, "Fizz"),
        (5, "Buzz"),
        (7, "7"),
        (15, "FizzBuzz"),
        (100, "Buzz"),
        (0, "FizzBuzz"),
        (-3, "Fizz"),
    ]:
        yield f


@pytest.mark.parametrize("value, expected", fizzbuzz_cases())
def test_fizzbuzz(value, expected):
    assert fizzbuzz(value) == expected
