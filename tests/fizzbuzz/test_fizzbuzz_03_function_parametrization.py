# test_fizzbuzz_03_function_parametrization

import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.smoke
@pytest.mark.fizzbuzz
@pytest.mark.parametrize(
    "value, expected",
    [
        (3, "Fizz"),
        (5, "Buzz"),
        (7, "7"),
        (15, "FizzBuzz"),
        (100, "Buzz"),
        (0, "FizzBuzz"),
        (-3, "Fizz"),
    ],
)
def test_fizzbuzz(value, expected):
    assert fizzbuzz(value) == expected
