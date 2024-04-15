def solve_n_queens(n):
    solutions = []
    positions = [-1] * n  # Keeps track of queen placement in columns

    def solve(row):

        if row == n:
            solution = [(r+1, col+1) for r, col in enumerate(positions) if col != -1]
            solutions.append(solution)  # Add a list of positions in the solution
            return

        for col in range(n):
            if is_safe(row, col, positions):
                positions[row] = col
                solve(row + 1)
                positions[row] = -1  # Backtrack

    def is_safe(row, col, positions):

        for r in range(row):
            if positions[r] == col or abs(row - r) == abs(positions[r] - col):
                return False
        return True

    solve(0)
    return solutions

# Example usage
n = int(input())
solutions = solve_n_queens(n)
if len(solutions) > 0:
    for solution in solutions:
        print(f'[{solution[0]} {solution[1]} {solution[2]} {solution[3]}]')
else:
    print('No solution found.')
