def solve_n_queens(n):
  solutions = []
  cols = [-1] * n  # Keeps track of queen placement in columns

  def solve(row):

    if row == n:
      solution = [[r, col] for r, col in enumerate(cols) if col != -1]
      solutions.append(solution)  # Add a list of positions in the solution
      return

    for col in range(n):
      if is_safe(row, col, cols):
        cols[row] = col
        solve(row + 1)
        cols[row] = -1  # Backtrack

  def is_safe(row, col, cols):

    for i in range(row):
      if cols[i] == col or abs(row - i) == abs(cols[i] - col):
        return False
    return True

  solve(0)
  return solutions

# Example usage
n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n} queens: {len(solutions)}")

if solutions:
  for solution in solutions:
    print("Solution:")
    for row, col in solution:
      print(f"Queen at row {row+1}, column {col+1}")  # User-friendly output (1-based indexing)
