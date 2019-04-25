#! /usr/bin/env python

from . import base


class TestTheTrip(base.TestCase):

    program_path = "the_trip.py"

    def setUp(self):
        _input = (
            b"3",
            b"10.0",
            b"20.0",
            b"30.0",
            b"4",
            b"15.00",
            b"15.01",
            b"3.00",
            b"3.01",
            b"0"
        )
        expected_output = (
            b"$10.00",
            b"$11.99"
        )
        _input_combined = b"\n".join(_input)
        expected_output_combined = b"\n".join(expected_output)

        self.inputs_and_expected_outputs = (
            (_input_combined, expected_output_combined),
        )
