import sys

def padding(matrix, half_height=None):
    if half_height is None:
        max_lengths = [len(str(max(col, key=len))) for col in zip(*matrix)]
    else:
        max_lengths = [len(str(max(col, key=len))) for col in zip(*matrix[:height])]
    for row_idx, row in enumerate(matrix):
        matrix[row_idx] = [(" " * (max_length - len(item))) + item
                          for item, max_length in zip(row, max_lengths)]
    return matrix

height, width = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(height):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)
if height * width < 1000000:
    matrix = padding(matrix)
else:
    matrix = padding(matrix, height // 25)
for row in matrix:
    sys.stdout.write(' '.join(x for x in row))
    sys.stdout.write('\n')