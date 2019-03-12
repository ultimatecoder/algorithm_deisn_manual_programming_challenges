#! /usr/bin/env python
"""
The Trip

Definition

A group of students are members of a club that travels annually to different
lo- cations. Their destinations in the past have included Indianapolis,
Phoenix, Nashville, Philadelphia, San Jose, and Atlanta. This spring they are
planning a trip to Eindhoven.  The group agrees in advance to share expenses
equally, but it is not practical to share every expense as it occurs. Thus
individuals in the group pay for particular things, such as meals, hotels, taxi
rides, and plane tickets. After the trip, each student’s expenses are tallied
and money is exchanged so that the net cost to each is the same, to within one
cent. In the past, this money exchange has been tedious and time consuming.
Your job is to compute, from a list of expenses, the minimum amount of money
that must change hands in order to equalize (within one cent) all the students’
costs.

Input

Standard input will contain the information for several trips. Each trip
consists of a line containing a positive integer n denoting the number of
students on the trip. This is followed by n lines of input, each containing the
amount spent by a student in dollars and cents. There are no more than 1000
students and no student spent more than $10,000.00. A single line containing 0
follows the information for the last trip.

Output

For each trip, output a line stating the total amount of money, in dollars and
cents, that must be exchanged to equalize the students’ costs.

Sample Input

3
10.00
20.00
30.00
4
15.00
15.01
3.00
3.01
0

Sample Output

$10.00
$11.99
"""

import sys
import statistics


def validate_total_students(value):
    """Validates that total number of students are below 1000"""
    return (type(value) is int) and value < 1000 and value >= 0


def validate_expense(value):
    """Validate expense that it is below $10, 000"""
    return (type(value) is float) and (value < 10_000) and (value >= 0)


def calculate_minimum_exchange(expenses):
    average_expense = statistics.mean(expenses)
    below_average_expenses = list(
        filter(lambda e: e < average_expense, expenses)
    )
    differences = list(
        map(lambda e: average_expense - e, below_average_expenses)
    )
    return sum(differences)


def calculate_minimum_exchanges(all_expenses):
    minimum_exchanges = []
    for expenses in all_expenses:
        minimum_exchange = calculate_minimum_exchange(expenses)
        minimum_exchanges.append(minimum_exchange)
    return minimum_exchanges


if __name__ == "__main__":
    total_students = None
    all_trip_expenses = []
    while total_students != True:
        total_students = int(input(""))
        if not validate_total_students(total_students):
            print("Invalid students value.")
            sys.exit(1)
        if total_students == 0:
            break
        single_trip_expenses = []
        for i in range(total_students):
            expense = float(input(""))
            if not validate_expense(expense):
                print("Invalid expense value")
                sys.exit(1)
            single_trip_expenses.append(expense)
        all_trip_expenses.append(single_trip_expenses)
    minimum_exchanges = calculate_minimum_exchanges(all_trip_expenses)
    for minimum_exchange in minimum_exchanges:
        print(f"${minimum_exchange}")
