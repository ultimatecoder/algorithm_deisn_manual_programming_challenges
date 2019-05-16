#! /usr/bin/env python

import unittest

import puzzle_problem


class TestPuzzleProblem(unittest.TestCase):

    def test_is_puzzle_solved(self):
        sample_board_positions = (
            (
                [
                    [2, 3, 4, 0],
                    [1, 5, 7, 8],
                    [9, 6, 10, 12],
                    [13, 14, 11, 15]
                ], False
            ),
            (
                [
                    [13, 1, 2, 4],
                    [5, 0, 3, 7],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ], False
            ),
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 0]
                ], True
            )
        )

        for board, expected_answer in sample_board_positions:
            with self.subTest(board=board, expected_answer=expected_answer):
                self.assertEqual(
                    puzzle_problem.is_puzzle_solved(board),
                    expected_answer
                )

    def test_swap_left_for_impossible_values(self):
        sample_board_positions = (
            (
                [
                    [0, 3, 4, 2],
                    [1, 5, 7, 8],
                    [9, 6, 10, 12],
                    [13, 14, 11, 15]
                ]
            ),
            (
                [
                    [13, 1, 2, 4],
                    [0, 7, 3, 5],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ]
            ),
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [0, 14, 15, 13]
                ]
            )
        )

        for board in sample_board_positions:
            with self.subTest(board=board):
                self.assertIsNone(puzzle_problem.swap_left(board))

    def test_swap_left_for_possible_values(self):
        sample_board_positions = (
            (
                [
                    [2, 3, 4, 0],
                    [1, 5, 7, 8],
                    [9, 6, 10, 12],
                    [13, 14, 11, 15]
                ],
                [
                    [2, 3, 0, 4],
                    [1, 5, 7, 8],
                    [9, 6, 10, 12],
                    [13, 14, 11, 15]
                ]
            ),
            (
                [
                    [13, 1, 2, 4],
                    [3, 7, 0, 5],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ],
                [
                    [13, 1, 2, 4],
                    [3, 0, 7, 5],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ]
            ),
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [15, 14, 0, 13]
                ],
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [15, 0, 14, 13]
                ]
            )
        )

        for board, expected_board in sample_board_positions:
            with self.subTest(board=board, expected_board=expected_board):
                self.assertListEqual(
                    puzzle_problem.swap_left(board),
                    expected_board
                )

    def test_swap_right_for_impossible_values(self):
        sample_board_positions = (
            (
                [
                    [2, 3, 4, 0],
                    [1, 5, 7, 8],
                    [9, 6, 10, 12],
                    [13, 14, 11, 15]
                ]
            ),
            (
                [
                    [13, 1, 2, 4],
                    [5, 7, 3, 0],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ]
            ),
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 0]
                ]
            )
        )

        for board in sample_board_positions:
            with self.subTest(board=board):
                self.assertIsNone(puzzle_problem.swap_right(board))

    def test_swap_right_for_possible_values(self):
        sample_board_positions = (
            (
                [
                    [0, 3, 4, 2],
                    [1, 5, 7, 8],
                    [9, 6, 10, 12],
                    [13, 14, 11, 15]
                ],
                [
                    [3, 0, 4, 2],
                    [1, 5, 7, 8],
                    [9, 6, 10, 12],
                    [13, 14, 11, 15]
                ]
            ),
            (
                [
                    [13, 1, 2, 4],
                    [3, 7, 0, 5],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ],
                [
                    [13, 1, 2, 4],
                    [3, 7, 5, 0],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ]
            ),
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [15, 14, 0, 13]
                ],
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [15, 14, 13, 0]
                ]
            )
        )

        for board, expected_board in sample_board_positions:
            with self.subTest(board=board, expected_board=expected_board):
                self.assertListEqual(
                    puzzle_problem.swap_right(board),
                    expected_board
                )


    def test_swap_up_for_impossible_values(self):
        board = [
            [2, 3, 4, 0],
            [1, 5, 7, 8],
            [9, 6, 10, 12],
            [13, 14, 11, 15]
        ]

        self.assertIsNone(puzzle_problem.swap_up(board))

    def test_swap_up_for_possible_values(self):
        sample_board_positions = (
            (
                [
                    [13, 1, 2, 4],
                    [3, 7, 0, 5],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ],
                [
                    [13, 1, 0, 4],
                    [3, 7, 2, 5],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ]
            ),
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [15, 14, 0, 13]
                ],
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 0, 12],
                    [15, 14, 11, 13]
                ]
            )
        )

        for board, expected_board in sample_board_positions:
            with self.subTest(board=board, expected_board=expected_board):
                self.assertListEqual(
                    puzzle_problem.swap_up(board),
                    expected_board
                )

    def test_swap_down_for_impossible_values(self):
        board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]

        self.assertIsNone(puzzle_problem.swap_down(board))

    def test_swap_down_for_possible_values(self):
        sample_board_positions = (
            (
                [
                    [0, 3, 4, 2],
                    [1, 5, 7, 8],
                    [9, 6, 10, 12],
                    [13, 14, 11, 15]
                ],
                [
                    [1, 3, 4, 2],
                    [0, 5, 7, 8],
                    [9, 6, 10, 12],
                    [13, 14, 11, 15]
                ]
            ),
            (
                [
                    [13, 1, 2, 4],
                    [3, 7, 0, 5],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ],
                [
                    [13, 1, 2, 4],
                    [3, 7, 10, 5],
                    [9, 6, 0, 12],
                    [15, 8, 11, 14]
                ]
            ),
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 0, 11, 12],
                    [15, 14, 10, 13]
                ],
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 14, 11, 12],
                    [15, 0, 10, 13]
                ]
            )
        )

        for board, expected_board in sample_board_positions:
            with self.subTest(board=board, expected_board=expected_board):
                self.assertListEqual(
                    puzzle_problem.swap_down(board),
                    expected_board
                )

    def test_solve_puzzle(self):
        sample_inputs = (
            (
                [
                    [2, 3, 4, 0],
                    [1, 5, 7, 8],
                    [9, 6, 10, 12],
                    [13, 14, 11, 15]
                ], "LLLDRDRDR"
            ),
            (
                [
                    [13, 1, 2, 4],
                    [5, 0, 3, 7],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ],
                "This puzzle is not solvable."
            )
        )

        for board, expected_answer in sample_inputs:
            self.assertEqual(
                puzzle_problem.solve_puzzle(board=board),
                expected_answer
            )

    def test_score(self):
        sample_boards_and_expected_answer = (
            (
                [
                    [2, 3, 4, 0],
                    [1, 5, 7, 8],
                    [9, 6, 10, 12],
                    [13, 14, 11, 15]
                ], 6

            ),
            (
                [
                    [13, 1, 2, 4],
                    [5, 0, 3, 7],
                    [9, 6, 10, 12],
                    [15, 8, 11, 14]
                ], 4
            ),
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 0]
                ], 16
            ),
            (
                [
                    [0, 15, 14, 13],
                    [12, 11, 10, 9],
                    [8, 7, 6, 5],
                    [4, 3, 2, 1]
                ], 0
            )
        )

        for board, expected_answer in sample_boards_and_expected_answer:
            with self.subTest(board=board, expected_answer=expected_answer):
                self.assertEqual(
                    puzzle_problem.calculate_score(board),
                    expected_answer
                )
