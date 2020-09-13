# test_fizzbuzz_08_fixture.py

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


@pytest.fixture(params=FIZZ_BUZZ_TEST_CASES)
def a_case(request):
    return request.param


@pytest.mark.smoke
def test_fix(a_case):
    value, expected = a_case
    assert fizzbuzz(value) == expected
