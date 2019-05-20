#! /usr/bin/env python
"""
Problem

    A turtle named Mack, to avid being cracked, has enlisted your advice as to
    the order in which turtles should be stacked to form Yertle the Turtle's
    throne. Each of the 5,607 turtles ordered by Yertle has a different weight
    and strength. Your task is to build the largest stack of turtles possible.

Input

    Standard input consists of several lines, each containing a pair of
    integers seperated by one or more space characters, specifying the weight
    and strength of a turtle. The weight of the turtle is in grams. The
    strength, also in grams, is the turtle's overall carrying capacity,
    including its own weight. That is, a turtle weighing 300 g with a strength
    of 1,000 g can carry 700 g of turtles on its back. There are at most 5,607
    turtles.

Output

    Your output is a single integer indicating the maximum number of turtles
    that can be stacked without exceeding the strength of any one.

Sample Input

    300 1000
    1000 1200
    200 600
    100 101

Sample Output

    3
"""
import math


def remaining_turtles(turtles, index):
    copy_of_turtles = turtles[:]
    del copy_of_turtles[index]
    return copy_of_turtles


def calculate_turtle_sequence(turtles, capacity=None):
    current_turtle_sequence = 1
    number_of_turtles_in_stack = [0]
    for index, turtle in enumerate(turtles):
        weight, total_capacity = turtle
        if capacity is None:
            number_of_turtles = (
                current_turtle_sequence + calculate_turtle_sequence(
                    turtles=remaining_turtles(turtles, index),
                    capacity=(total_capacity - weight)
                )
            )
            number_of_turtles_in_stack.append(number_of_turtles)
        elif weight <= capacity:
                remaining_capacity = min(
                    (capacity - weight), (total_capacity - weight)
                )
                number_of_turtles = (
                    current_turtle_sequence + calculate_turtle_sequence(
                        turtles=remaining_turtles(turtles, index),
                        capacity=remaining_capacity
                    )
                )
                number_of_turtles_in_stack.append(number_of_turtles)
    return max(number_of_turtles_in_stack)


if __name__ == "__main__":
    turtles = [
        [200, 600],
        [100, 101],
        [1000, 1200],
        [300, 1000],
    ]
    print(calculate_turtle_sequence(turtles))
