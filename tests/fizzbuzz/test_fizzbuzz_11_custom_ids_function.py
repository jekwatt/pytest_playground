# test_fizzbuzz_11_custom_ids_function.py

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


def idfn(a_case):
    value, expected = a_case
    return f"{value}-{expected}"


@pytest.fixture(params=FIZZ_BUZZ_TEST_CASES, ids=idfn)
def a_case(request):
    return request.param


@pytest.mark.fizzbuzz
def test_fix(a_case):
    value, expected = a_case
    assert fizzbuzz(value) == expected
