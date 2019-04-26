#! /usr/bin/env python

import unittest

import the_trip


class TestTheTrip(unittest.TestCase):

    def test_validate_total_students_for_valid_values(self):
        values = (1, 12, 999, 100, 0)
        for value in values:
            with self.subTest(value=value):
                self.assertTrue(the_trip.validate_total_students(value))

    def test_validate_total_students_for_invalid_values(self):
        values = (-1, 1001, 23.44, "sdf")
        for value in values:
            with self.subTest(value=value):
                self.assertFalse(the_trip.validate_total_students(value))

    def test_validate_expense_for_valid_values(self):
        values = (1.00, 13.00, 1000.00, 9999.00)
        for value in values:
            with self.subTest(value=value):
                self.assertTrue(the_trip.validate_expense(value))

    def test_valudate_expense_for_invalid_values(self):
        values = (-11.00, -1.00, 10000.00, "srt")
        for value in values:
            with self.subTest(value=value):
                self.assertFalse(the_trip.validate_expense(value))

    def test_calculate_minimum_exchange(self):
        expenses_and_expected_minimum_exchanges = (
            #(list of expenses, minimum_exchange)
            ([10.00, 20.00, 30.00], 10.00),
            ([15.00, 15.01, 3.00, 3.01], 11.999999999999998)
        )
        for expenses, expected_minimum_exchange in (
            expenses_and_expected_minimum_exchanges
        ):
            with self.subTest(
                expenses=expenses,
                expected_minimum_exchange=expected_minimum_exchange
            ):
                self.assertEqual(
                    the_trip.calculate_minimum_exchange(expenses),
                    expected_minimum_exchange
                )

    def test_calculate_minimum_exchanges(self):
        all_expenses = [
            [10.00, 20.00, 30.00], [15.00, 15.01, 3.00, 3.01]
        ]
        expected_minimum_exchanges = [ 10.00, 11.999999999999998]
        self.assertListEqual(
            the_trip.calculate_minimum_exchanges(all_expenses),
            expected_minimum_exchanges
        )
