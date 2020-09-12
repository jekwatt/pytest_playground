# test_fizzbuzz_05_parameters_from_function

import pytest

from fizzbuzz import fizzbuzz


def fizzbuzz_cases():
    return [
        (3, "Fizz"),
        (5, "Buzz"),
        (7, "7"),
        (15, "FizzBuzz"),
        (100, "Buzz"),
        (0, "FizzBuzz"),
        (-3, "Fizz"),
    ]


@pytest.mark.parametrize("value, expected", fizzbuzz_cases())
def test_fizzbuzz(value, expected):
    assert fizzbuzz(value) == expected
