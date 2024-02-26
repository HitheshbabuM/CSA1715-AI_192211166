def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, row, num_queens):
    if row == num_queens:
        return True

    for col in range(num_queens):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_queens(board, row + 1, num_queens):
                return True
            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "-" for cell in row))

def solve_n_queens(num_queens):
    board = [[0 for _ in range(num_queens)] for _ in range(num_queens)]
    if solve_queens(board, 0, num_queens):
        print_board(board)
    else:
        print("No solution exists.")

num_queens = int(input("Enter the number of queens: "))
solve_n_queens(num_queens)
