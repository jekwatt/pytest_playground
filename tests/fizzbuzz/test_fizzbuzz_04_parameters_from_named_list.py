# test_fizzbuzz_04_parameters_from_named_list

import pytest

from fizzbuzz import fizzbuzz

FIZZ_BUZZ_TEST_CASES = [
    (3, "Fizz"),
    (5, "Buzz"),
    (7, "7"),
    (15, "FizzBuzz"),
    (100, "Buzz"),
    (0, "FizzBuzz"),
    (-3, "Fizz"),
]


@pytest.mark.parametrize("value, expected", FIZZ_BUZZ_TEST_CASES)
def test_fizzbuzz(value, expected):
    assert fizzbuzz(value) == expected
