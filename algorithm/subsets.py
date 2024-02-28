# Input arguments
H, W, K = map(int, input().split())

# Declare matrix
matrix = []

# Input matrix
for _ in range(H):
    row = input("Nhập dòng {}: ".format(_ + 1))
    matrix.append(row)
TOTAL = sum(row.count('#') for row in matrix)

def get_all_possible_line(H, W):
    """
    Args:
        H: height
        W: width
    Returns:
        list_lines: list of lines
    """
    list_lines = []
    for h in range(H):
        list_lines.append(('row', h))
    for w in range(W):
        list_lines.append(('col', w))

    return list_lines

def get_subsets(list_lines):
    """
    Args:
        lines: Initial list.
    Returns:
        subsets: List contain of subsets.
    """
    subsets = []
    for i in range(2**len(list_lines)):
        subset = []
        for j in range(len(list_lines)):
            if (i >> j) & 1:
                subset.append(list_lines[j])
        subsets.append(subset)
    return subsets

def check(matrix, lines):
    """
    Args:
        matrix: Matrix input
        lines: List of line
    Returns:
        count: Special char in these line
    """
    count = 0
    rows = []
    cols = []
    # Counting
    for line in lines:
        if line[0] == 'row':
            rows.append(line[1])
            count += sum(row.count('#') for indx, row in enumerate(matrix) if indx == line[1])
        else:
            cols.append(line[1])
            count += sum(row[int(line[1])] == '#' for row in matrix)
    # Avoid duplicate
    for row in rows:
        for col in cols:
            if matrix[row][col] == '#':
                count  -= 1
    
    return count

def solve(matrix, subsets):
    """
    Args:
        matrix: Matrix input
        subset: List of subset
    Returns:
        count: Number of solve
    """
    count = 0
    for lines in subsets:
        remove = check(matrix, lines)
        remain = TOTAL - remove
        if remain == K:
            count += 1
    return count

lst = get_all_possible_line(H, W)
subsets = get_subsets(lst)
result = solve(matrix, subsets)
print(result)