def solve_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row, board):
        if row == n:
            return [board[:]]
        solutions = []
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solutions.extend(place_queens(n, row + 1, board))
        return solutions

    return place_queens(n, 0, [-1]*n)

def print_board(board):
    n = len(board)
    for col in board:
        row = ['.'] * n
        row[col] = 'Q'
        print(' '.join(row))

n = int(input("Enter n value: "))
solutions = solve_queens(n)
print(f"Found {len(solutions)} solutions for {n} queens:")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    print_board(solution)
    print()