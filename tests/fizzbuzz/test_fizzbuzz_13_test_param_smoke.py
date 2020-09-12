# test_fizzbuzz_13_test_param_smoke.py

import pytest

from fizzbuzz import fizzbuzz

smoke = pytest.mark.smoke

FIZZ_BUZZ_TEST_CASES = [
    (3, "Fizz"),
    (5, "Buzz"),
    pytest.param(7, "7", id='7'),
    (15, "FizzBuzz"),
    pytest.param(100, "Buzz", marks=smoke),
    pytest.param(0, "FizzBuzz", marks=smoke),
    pytest.param(-3, "Fizz", marks=smoke),
]


@pytest.mark.parametrize("value, expected", FIZZ_BUZZ_TEST_CASES)
def test_fizzbuzz(value, expected):
    assert fizzbuzz(value) == expected
