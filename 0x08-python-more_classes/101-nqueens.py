#!/usr/bin/python3


import sys

def nqueens(N):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == N:
            print('[' + ', '.join(str(c + 1) for c in board) + ']')
        else:
            for col in range(N):
                if is_valid(board, row, col):
                    board[row] = col
                    solve(board, row + 1)

    if not isinstance(N, int):
        print('N must be a number')
        sys.exit(1)
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = [-1] * N
    solve(board, 0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    nqueens(N)

