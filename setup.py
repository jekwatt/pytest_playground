from setuptools import setup, find_packages

setup(
    name='fizzbuzz',
    version='0.0.1',
    description='Very simple program, often used in software developer job interviews"
    author='Jennifer Watt',
    author_email='',
    url='https://github.com/jekwatt/pytest_playground',
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
)
