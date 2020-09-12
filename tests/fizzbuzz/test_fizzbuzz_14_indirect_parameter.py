# test_fizzbuzz_14_indirect_parameter.py

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


@pytest.fixture()
def expected(request):
    if request.param == "FizzBuzz":
        print("\nthis is one of the FizzBuzz test cases")
    return request.param


@pytest.mark.parametrize("value, expected", FIZZ_BUZZ_TEST_CASES,
                          indirect=["expected"])
def test_fizzbuzz(value, expected):
    assert fizzbuzz(value) == expected
