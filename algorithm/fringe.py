import sys
import math

def find_fringe(height, width):
    parent_lst = []
    num_fringe = math.ceil(min(height, width)/2)
    for edge_idx in range(num_fringe):
        child_lst = []
        x = edge_idx
        y = edge_idx
        while True:
            child_lst.append((x, y))
            if x == edge_idx and y != width - edge_idx - 1:
                y += 1
            elif y == width - edge_idx - 1 and x != height - edge_idx - 1:
                x += 1
            elif x == height - edge_idx - 1 and y != edge_idx:
                y -= 1
            elif y == edge_idx and x != edge_idx:
                x -= 1
            if (x, y) in child_lst:
                break
        parent_lst.append(child_lst)
    return parent_lst
        
def solve(height, width, matrix):

    addresses = find_fringe(height, width)
    new_matrix = [[0 for _ in range(width)] for _ in range(height)]

    for idx, address in enumerate(addresses):
        if idx % 2 == 0:
            new_address = address[-1:] + address[:-1]
        else:
            new_address = address[1:] + address[:1]

        for new, old in zip(new_address, address):
            new_matrix[old[0]][old[1]] = matrix[new[0]][new[1]]

    for row in new_matrix:
        sys.stdout.write(' '.join(str(x) for x in row))
        sys.stdout.write('\n')

height, width = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(height):
    row = list(map(str.strip, sys.stdin.readline().split()))
    matrix.append(row)
if height == 1 and width == 1:
    sys.stdout.write(str(matrix[0][0]))
else:
    solve(height, width, matrix)