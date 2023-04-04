#!/usr/bin/python3
"""
Module that contains the solution to the N Queens puzzle.
"""

import sys


def is_valid_position(board, row, col):
    """
    Check if the position (row, col) on the board is a valid position to place a queen.

    Args:
        board (list[list[int]]): the board where the queens are being placed.
        row (int): the row index.
        col (int): the column index.

    Returns:
        bool: True if it's a valid position, False otherwise.
    """
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there's a queen in the diagonal going up-left
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there's a queen in the diagonal going up-right
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i][j] == 1:
            return False

    # If all checks passed, it's a valid position
    return True


def n_queens(board, row):
    """
    Recursive function that finds a solution to the N Queens puzzle.

    Args:
        board (list[list[int]]): the board where the queens are being placed.
        row (int): the row index.

    Returns:
        None
    """
    # Base case: if all rows are filled, we found a solution
    if row == len(board):
        # Print the solution
        print([[i, j] for i, row in enumerate(board) for j, val in enumerate(row) if val == 1])
        return

    # For each column in the current row, try to place a queen
    for col in range(len(board)):
        if is_valid_position(board, row, col):
            # If it's a valid position, place the queen and move to the next row
            board[row][col] = 1
            n_queens(board, row+1)
            board[row][col] = 0  # backtrack


if __name__ == "__main__":
    # Check if the user called the program with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty board of size N x N
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Start the recursion
    n_queens(board, 0)
