#! /usr/bin/env python

import unittest

from . import utilities


class TestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.utilities = utilities.TestCase()
        return super().__init__(*args, **kwargs)

    def test_program_produces_expected_output_against_given_input(self):
        """Asserts program is producing expected output

        This test case will be automatically invoked if you will inherit this
        class. The test case is dependent on below class level attributes.

        * python_file_path            : Is a path to a python program which
                                        will be invoked for asserting output of
                                        it.
        * inputs_and_expected_outputs : A tuple or any python iterable object.
                                        Each member is a combination of input
                                        and expected output. First member is
                                        input which will be provided to the
                                        `STDIN` of the program and second
                                        argument is the expected value from the
                                        program. Expected output value will be
                                        compared with `STDOUT` value given by
                                        the program.
        """
        for _input, expected_output in self.inputs_and_expected_outputs:
            self.utilities.assertPythonOutput(
                self.program_path, _input, expected_output
            )
