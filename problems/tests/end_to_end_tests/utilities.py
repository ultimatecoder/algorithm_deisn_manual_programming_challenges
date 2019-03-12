#! /usr/bin/env python

import subprocess
import unittest


class TestCase(unittest.TestCase):

    def assertOutput(
        self, program_argument, input_stdin, expected_output, timeout=15,
        strip=True
    ):
        """Asserts expected output for given input

        * `program_argument` : An command with expected `args` in Python list
                               type.
        * `input_stdin`      : A value which will be feeded to `STDIN` of the
                               invoked progra.
        * `expected_output`  : Expected output value from the invoked program.
                               It will be compared with the `STDOUT` of the
                               program.
        * `strip`            : It will strip the `STDOUT` value before
                               comparing it with the `expected_output` value.
                               By default it is `True`. Making it `False` will
                               not string the `STDOUT` value.

        Call this method to assert the expected output value of your program.
        It will feed given input_stdin to the `STDIN` of the program. Waits for
        the given time. Asserts the output produced by the program (STDOUT)
        with the expected output. If it fails to produce during the given time
        frame.
        """
        with subprocess.Popen(
            program_argument, stdin=subprocess.PIPE, stdout=subprocess.PIPE
        ) as p:
            out, err = p.communicate(input=input_stdin, timeout=15)
            if strip:
                out = out.strip()
            self.assertEqual(out, expected_output)

    def assertPythonOutput(
        self, program_path, input_stdin, expected_output, timeout=15, args=[]
    ):
        """Asserts expected output for given input_stdin

        * `python_program`     : File path of the Python program.
        * `input_stdin`        : A value which will be feeded to `STDIN` of the
                                 invoked progra.
        * `expected_output`    : Expected output value from the invoked
                                 program. It will be compared with the
                                 `STDOUT` of the program.
        * `timeout`            : Waits for the program to produce an output in
                                 given time. Fires an exception if the program
                                 is failed to return any output during
                                 mentioned time. It accepts time in secounds.

        Call this method to assert the expected output value of your python
        program. It is an wrapper over `assertOutput` method of this class. Use
        this method when you want to test your Python programs.
        """
        program_argument = ["python", program_path]
        program_argument.extend(args)
        return self.assertOutput(
            program_argument, input_stdin, expected_output
        )
