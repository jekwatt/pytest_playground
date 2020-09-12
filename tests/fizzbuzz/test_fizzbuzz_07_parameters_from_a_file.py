# test_fizzbuzz_07_parameters_from_a_file

import csv
import pytest
from pathlib import Path

from fizzbuzz import fizzbuzz

p = Path.cwd()
FIZZBUZZ_DATA_FILE_NAME = p / "tests" / "fizzbuzz" / "fizzbuzz_data.csv"


def fizzbuzz_cases():
    with open(FIZZBUZZ_DATA_FILE_NAME) as csvfile:
        for value, expected in csv.reader(csvfile):
            yield (int(value), expected)

@pytest.mark.parametrize("value, expected", fizzbuzz_cases())
def test_fizzbuzz(value, expected):
    assert fizzbuzz(value) == expected
