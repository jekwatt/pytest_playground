# test_fizzbuzz_02_dont_do_thi

from fizzbuzz import fizzbuzz


# Don't do this!
def test_fizzbuzz():
    FIZZBUZZ_TEST_CASES = [
        (3, "Fizz"),
        (5, "Buzz"),
        (7, "7"),
        (15, "FizzBuzz"),
        (100, "Buzz"),
        (0, "FizzBuzz"),
        (-3, "Fizz"),
    ]
    for value, expected in FIZZBUZZ_TEST_CASES:
        assert fizzbuzz(value) == expected
