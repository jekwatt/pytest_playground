# test_fizzbuzz_01_without_parametrization

from fizzbuzz import fizzbuzz


def test_fizz():
    assert fizzbuzz(3) == "Fizz"


def test_buzz():
    assert fizzbuzz(5) == "Buzz"


def test_fizzbuzz():
    assert fizzbuzz(0) == "FizzBuzz"


def test_invalid():
    assert fizzbuzz("Zero") == None
