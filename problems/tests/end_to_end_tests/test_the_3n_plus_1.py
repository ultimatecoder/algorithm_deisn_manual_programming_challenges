#! /usr/bin/env python

from . import base


class TestThe3nPlus1(base.TestCase):
    """Assert The 3n + 1 problem is producing appropriate output"""

    inputs_and_expected_outputs = (
        (b"1 10", b"1 10 20"),
        (b"100 200", b"100 200 125"),
        (b"201 210", b"201 210 89"),
        (b"900 1000", b"900 1000 174")
    )

    program_path = "the_3n_plus_1.py"
