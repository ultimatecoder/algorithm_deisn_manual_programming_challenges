"""
 The 3n + 1 Problem

 Description

 Consider the following algorithm to generate a sequence of
 numbers. Start with an integer n. If n is even, divide by 2. If n is odd,
 multiply by 3 and add 1. Repeat this process with the new value of n,
 terminating when n = 1. For example, the following sequence of numbers will
 be generated for n = 22.

 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

 It is conjectured (but not yet proven) that this algorithm will terminate at
 n = 1 for every integer n. Still, the conjecture holds for all integers up
 to at least 1, 00, 000.

 For an input n, the cycle-length of n is the number of numbers generated
 up to and including the 1. In the example above, the cycle length of 22 is
 16. Given any two numbers i and j, you are to determine the maximum cycle
 length over all numbers between i and j, including both endpoints.
"""

import sys


def validate_number(number):
    """Validate that the number is 0 < number < 1, 000, 000."""
    return number > 0 and number < 1_000_000


def calculate_cycle(number):
    """Calculates cycle for given number

    Algorithm:
        Step-1: If number is even then `divide it by 2 or go to Step-2
        Step-2: If number is odd then multiply it by 3 and add 1
        Step-3: Repeat this calculation until number is 1.
    """
    cycles = []
    while number != 1:
        cycles.append(number)
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
    cycles.append(1)
    return cycles


def calculate_cycle_length(number):
    """Calculates a cycles-length for given number."""
    return len(calculate_cycle(number))


def calculate_maximum_cycle_length(i, j):
    """Returns maximum cycle length between numbers i and j.

    For example, i=1 and j=10 then it will return 20.
    """
    maximum_cycle_length = 0
    for number in range(i+1, j):
        cycle_length = calculate_cycle_length(number)
        if cycle_length > maximum_cycle_length:
            maximum_cycle_length = cycle_length
    return maximum_cycle_length


if __name__ == "__main__":
    i_and_j = input("")
    i, j = map(int, i_and_j.split(" "))

    error_message = 'Please enter value of "{}" between 0 to 1, 000, 000.'
    for value, variable_name in [(i, 'i'), (j, 'j')]:
        if not validate_number(value):
            print(error_message.format(variable_name))
            sys.exit(1)

    maximum_cycle_length = calculate_maximum_cycle_length(i, j)
    print(i, j, maximum_cycle_length)
