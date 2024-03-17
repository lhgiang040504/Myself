'''import sys
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
height = 4
width = 1
matrix = [['1'], ['6'], ['7'], ['2']]
if height == 1 and width == 1:
    sys.stdout.write(str(matrix[0][0]))
elif height == 1:
    matrix[0] = matrix[0][-1:] + matrix[0][:-1]
    sys.stdout.write(' '.join(str(x) for x in matrix[0]))
elif width == 1:
    matrix = matrix[-1:] + matrix[:-1]
    for row in matrix:
        sys.stdout.write(' '.join(str(x) for x in row))
        sys.stdout.write('\n')
else:
    solve(height, width, matrix)
'''
import sys
import math

def find_fringe(height, width):
    parent_lst = []
    num_fringe = math.ceil(min(height, width) / 2)

    for edge_idx in range(num_fringe):
        child_lst = []
        x = edge_idx
        y = edge_idx

        # Top edge
        for j in range(y, width - edge_idx):
            child_lst.append((x, j))

        # Right edge
        for i in range(x + 1, height - edge_idx):
            child_lst.append((i, width - edge_idx - 1))

        # Bottom edge
        for j in range(width - edge_idx - 2, edge_idx-1, -1):
            if edge_idx == num_fringe-1:
                if (height - edge_idx - 1, j) not in child_lst:
                    child_lst.append((height - edge_idx - 1, j))
            else:
                child_lst.append((height - edge_idx - 1, j))

        # Left edge
        for i in range(height - edge_idx - 2, edge_idx, -1):
            if edge_idx == num_fringe-1:
                if ((i, edge_idx)) not in child_lst:
                    child_lst.append((i, edge_idx))
            else:
                child_lst.append((i, edge_idx))

        parent_lst.append(child_lst)

    return parent_lst
    
def sfind_fringe(height, width):
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
    if width == 1:
        addresses = sfind_fringe(height, width)
    else:
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