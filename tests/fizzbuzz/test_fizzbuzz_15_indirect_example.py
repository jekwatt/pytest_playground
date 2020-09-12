# test_fizzbuzz_15_indirect_example.py

import csv
import pytest
from pathlib import Path

from fizzbuzz import fizzbuzz

p = Path.cwd()
FIZZBUZZ_DATA_FILE_NAME = p / "tests" / "fizzbuzz" / "fizzbuzz_data.csv"


def fizzbuzz_cases():
    with open(FIZZBUZZ_DATA_FILE_NAME) as csvfile:
        for value, expected in csv.reader(csvfile):
            yield (value, expected)


@pytest.fixture()
def value(request):
    return int(request.param)


@pytest.mark.parametrize("value, expected", fizzbuzz_cases(),
                         indirect=["value"])
def test_fizzbuzz(value, expected):
    assert fizzbuzz(value) == expected
