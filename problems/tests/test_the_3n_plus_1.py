#! /usr/bin/env python

import unittest

import the_3n_plus_1


class TestThe3nPlus1(unittest.TestCase):

    def test_validate_number_for_valid_values(self):
        values = (1, 10, 11, 99, 999999)
        for value in values:
            self.assertTrue(the_3n_plus_1.validate_number(value))

    def test_validate_number_for_invalid_values(self):
        values = (-1, 1_000_0001, 2_000_000, 1_000_000_0)
        for value in values:
            self.assertFalse(the_3n_plus_1.validate_number(value))

    def test_calculate_cycles(self):
        number_and_expected_cycles = (
            # (number, [cycles])
            (1, [1]),
            (22, [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
            (34, [34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
            (999999, [
                999999, 2999998, 1499999, 4499998, 2249999, 6749998, 3374999,
                10124998, 5062499, 15187498, 7593749, 22781248, 11390624,
                5695312, 2847656, 1423828, 711914, 355957, 1067872, 533936,
                266968, 133484, 66742, 33371, 100114, 50057, 150172, 75086,
                37543, 112630, 56315, 168946, 84473, 253420, 126710, 63355,
                190066, 95033, 285100, 142550, 71275, 213826, 106913, 320740,
                160370, 80185, 240556, 120278, 60139, 180418, 90209, 270628,
                135314, 67657, 202972, 101486, 50743, 152230, 76115, 228346,
                114173, 342520, 171260, 85630, 42815, 128446, 64223, 192670,
                96335, 289006, 144503, 433510, 216755, 650266, 325133, 975400,
                487700, 243850, 121925, 365776, 182888, 91444, 45722, 22861,
                68584, 34292, 17146, 8573, 25720, 12860, 6430, 3215, 9646,
                4823, 14470, 7235, 21706, 10853, 32560, 16280, 8140, 4070,
                2035, 6106, 3053, 9160, 4580, 2290, 1145, 3436, 1718, 859,
                2578, 1289, 3868, 1934, 967, 2902, 1451, 4354, 2177, 6532,
                3266, 1633, 4900, 2450, 1225, 3676, 1838, 919, 2758, 1379,
                4138, 2069, 6208, 3104, 1552, 776, 388, 194, 97, 292, 146, 73,
                220, 110, 55, 166, 83, 250, 125, 376, 188, 94, 47, 142, 71,
                214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412,
                206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790,
                395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251,
                754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479,
                1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644,
                1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616,
                2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244,
                122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10,
                5, 16, 8, 4, 2, 1
            ])
        )

        for number, expected_cycles in number_and_expected_cycles:
            self.assertListEqual(
                the_3n_plus_1.calculate_cycle(number),
                expected_cycles
            )

    def test_calculate_cycle_length(self):
        number_and_expected_cycle_lengths = (
            # (number, cycle-length)
            (1, 1),
            (2, 2),
            (55,113),
            (999999, 259)
        )
        for number, expected_cycle_length in number_and_expected_cycle_lengths:
            self.assertEqual(
                the_3n_plus_1.calculate_cycle_length(number),
                expected_cycle_length
            )

    def test_calculate_maximum_cycles_length(self):
        values_and_expected_maximum_cycle_lengths = (
            ((1, 10), 20),
            ((100, 200), 125),
            ((201, 210), 89),
            ((900, 1000), 174)
        )

        for values, expected_maximum_cycle_length in (
            values_and_expected_maximum_cycle_lengths
        ):
            i, j = values
            self.assertEqual(
                the_3n_plus_1.calculate_maximum_cycle_length(i, j),
                expected_maximum_cycle_length
            )
