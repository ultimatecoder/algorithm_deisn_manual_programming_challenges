#! /usr/bin/env python
"""
Problem

    The 15-puzzle a very popular game; you have certainly seen it even if you
    don't know it by that name. It is constructed with 15 sliding tiles, each
    with a different number from 1 to 15, with all tiles packed into a 4 by 4
    frame with one tile missing. The object of the puzzle is to arrange the
    tiles so that they are ordered as below.

           _______________
           |1  |2 | 3  |4 |
           |5  |6 | 7  |8 |
           |9  |10| 11 |12|
           |13 |14| 15 |- |
           ----------------

    The only legal operation is to exchange the missing tile with one of the 2,
    3 or 4 tiles it shares an edge with. Consider the following sequence of
    moves:

    ________________
    |2  |12| 11 | 14|
    |6  |15| 10 | 5 |
    |3  |- | 9  | 13|
    |8  |7 | 1  | 4 |
    -----------------

    A random puzzle position

    ________________
    |2  |12| 11 | 14|
    |6  |15| 10 | 5 |
    |3  |9 | -  | 13|
    |8  |7 | 1  | 4 |
    ----------------

    The missing tile moves right (R)

    ________________
    |2  |12| 11 | 14|
    |6  |15| -  | 5 |
    |3  |9 | 10 | 13|
    |8  |7 | 1  | 4 |
    ----------------

    The missing tile moves upwards (U)

    ________________
    |2  |12| 11 | 14|
    |6  |- | 15 | 5 |
    |3  |9 | 10 | 13|
    |8  |7 | 1  | 4 |
    ----------------

    The missing tile moves left (L)

    We denote moves by the neighbor of the missing tile is swapped with it.
    Legal values are "R", "L", "U", "D" for right, left, up and down based on
    the movements of the hole.

    Given an initial configuration of a 15-puzzle you must determine a sequence
    of steps that take you to the final state. Each solvable 15-puzzle input
    require at most 45 steps to be solved with our judge solution; you are
    limited to using at most 50 steps to solve the puzzle.

Input

    The first line of the input contains an integer N indicating the number of
    puzzle set inputs. The next 4n lines contain N puzzle at four lines per
    puzzle. Zero denotes the missing tile.

Output

    For each input set you must produce one line of output. If the given
    initial configuration is not solvable, print the line "This puzzle is not
    solvable". If the puzzle is solvable, then print the move sequence as
    described above to solve the puzzle.

Sample Input

    2
    2 3 4 0
    1 5 7 8
    9 6 10 12
    13 14 11 15
    13 1 2 4
    5 0 3 7
    9 6 10 12
    15 8 11 14

Sample Output

    LLLDRDRDR
    This puzzle is not solvable.
"""
import copy


def is_puzzle_solved(board):
    """Returns True if all the elements are sorted.

    Below position of the board will be considered as the sorted.

    _______________
    |1  |2  |3  |4  |
    |5  |6  |7  |8  |
    |9  |10 |11 |12 |
    |13 |14 |15 |-  |
    -----------------

    Arguments:
        A 4 x 4 Matrix representing board.

    Returns:
        True or False
    """
    return calculate_score(board) == 16

def _find_position_of_missing_tile(board):
    """Returns the position of missing tile

    Arguments:
        Instance of 4 x 4 Matrix presenting elements
    Returns
        Tuple of row_index and column_index
    """
    total_rows = len(board)
    total_columns = len(board[0])
    for row_index in range(total_rows):
        for column_index in range(total_columns):
            if board[row_index][column_index] == 0:
                return (row_index, column_index)

def _swap_tiles(board, tile1, tile2):
    """Swaps tile1 with tile2 of the board"""
    row_index_1, column_index_1 = tile1
    row_index_2, column_index_2 = tile2
    board[row_index_1][column_index_1], board[row_index_2][column_index_2] = (
        board[row_index_2][column_index_2], board[row_index_1][column_index_1]
    )
    return board


def swap_left(board):
    """Swipes the missing tile with its left element

    Arguments:
        Instance of 4 x 4 Matrix representing board

    Returns
        New instance of board in which the missing tile is swapped with its
        left element.

        It returns None if the missing tile has no tile in its left.
    """
    modified_board = copy.deepcopy(board)
    first_column = 0
    modified_board = modified_board[:]
    row_of_middle_tile, column_of_middle_tile = (
        _find_position_of_missing_tile(modified_board)
    )

    row_of_left_tile = row_of_middle_tile
    column_of_left_tile = column_of_middle_tile - 1

    if column_of_left_tile < first_column:
        return None

    middle_tile = (row_of_middle_tile, column_of_middle_tile)
    left_tile = (row_of_left_tile, column_of_left_tile)
    modified_board = _swap_tiles(modified_board, middle_tile, left_tile)
    return modified_board


def swap_right(board):
    modified_board = copy.deepcopy(board)
    last_column = len(board[0]) - 1
    row_of_middle_tile, column_of_middle_tile = (
        _find_position_of_missing_tile(modified_board)
    )

    row_of_right_tile = row_of_middle_tile
    column_of_right_tile = column_of_middle_tile + 1

    if column_of_right_tile > last_column:
        return None

    middle_tile = (row_of_middle_tile, column_of_middle_tile)
    right_tile = (row_of_right_tile, column_of_right_tile)
    modified_board = _swap_tiles(modified_board, middle_tile, right_tile)
    return modified_board


def swap_up(board):
    modified_board = copy.deepcopy(board)
    first_row = 0
    row_of_middle_tile, column_of_middle_tile = (
        _find_position_of_missing_tile(modified_board)
    )

    row_of_up_tile = row_of_middle_tile - 1
    column_of_up_tile = column_of_middle_tile

    if row_of_up_tile < first_row:
        return None

    middle_tile = (row_of_middle_tile, column_of_middle_tile)
    up_tile = (row_of_up_tile, column_of_up_tile)
    modified_board = _swap_tiles(modified_board, middle_tile, up_tile)
    return modified_board


def swap_down(board):
    modified_board = copy.deepcopy(board)
    last_row = len(modified_board) - 1

    row_of_middle_tile, column_of_middle_tile = (
        _find_position_of_missing_tile(modified_board)
    )

    row_of_down_tile = row_of_middle_tile + 1
    column_of_down_tile = column_of_middle_tile

    if row_of_down_tile > last_row:
        return None

    middle_tile = (row_of_middle_tile, column_of_middle_tile)
    down_tile = (row_of_down_tile, column_of_down_tile)
    bard = _swap_tiles(modified_board, middle_tile, down_tile)
    return modified_board


def calculate_score(board):
    """Counts how many elements in a board are at their expected position.

    Higher value means there are many elements at their position. At any point
    lowest return value will be 0 and highest return value will be 16

    Arguments:
        Instance of 4 x 4 Matrix representing board elements

    Returns
        An integer value representing number of elements at their expected
        position in a given board.
    """
    solved_puzzle_board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

    total_rows = len(board)
    total_columns = len(board[0])
    score = 0

    for row_index in range(total_rows):
        for column_index in range(total_columns):
            expected_element = solved_puzzle_board[row_index][column_index]
            actual_element = board[row_index][column_index]
            if expected_element == actual_element:
                score += 1
    return score


def solve_puzzle(board, steps=[]):
    """Solves the given 15 puzzle


    Call this function by passing the constructed position of the board

    Arguments:
        * board: An instance of 4 x 4 Matrix representing board elements
        * steps: An instance of List representing perfromed steps on board.

    Returns:
        Combination of steps if the puzzle is solved under 50 steps. If not
        then it will return the string 'This puzzle is not solvable'.
    """

    if is_puzzle_solved(board):
        return ''.join(steps)

    if len(steps) == 50:
        return "This puzzle is not solvable."

    score = calculate_score(board)

    left_swapped_board = swap_left(board)

    if left_swapped_board and calculate_score(left_swapped_board) >= score:
        return solve_puzzle(left_swapped_board, steps+["L"])

    right_swapped_board = swap_right(board)

    if right_swapped_board and calculate_score(right_swapped_board) >= score:
        return solve_puzzle(right_swapped_board, steps+["R"])

    up_swapped_board = swap_up(board)

    if up_swapped_board and calculate_score(up_swapped_board) >= score:
        return solve_puzzle(up_swapped_board, steps+["U"])

    down_swapped_board = swap_down(board)

    if down_swapped_board and calculate_score(down_swapped_board) >= score:
        return solve_puzzle(down_swapped_board, steps+["D"])


if __name__ == "__main__":
    number_of_test_cases = int(input(''))

    for _ in range(number_of_test_cases):
        board = []
        for _ in range(4):
            row = input('').split(' ')
            row = list(map(int, row))
            board.append(row)
        output = solve_puzzle(board)
        print(output)
