# test_fizzbuzz_12_pytest_generate_tests.py

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


def pytest_generate_tests(metafunc):
    if "gen_case" in metafunc.fixturenames:
        metafunc.parametrize("gen_case",
                             FIZZ_BUZZ_TEST_CASES,
                             ids=idfn)


@pytest.mark.fizzbuzz
def test_gen(gen_case):
    value, expected = gen_case
    assert fizzbuzz(value) == expected
