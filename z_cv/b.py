"""
height = 5
width = 4
matrix = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16],
       [17, 18, 19, 20]]

height = 8
width = 1
matrix = [[238],
       [239],
       [240],
       [241],
       [242],
       [243],
       [244],
       [245]]
"""
height, width = map(int, input().split())
matrix = []
for _ in range(height):
    row = list(map(int, input().split()))
    matrix.append(row)

def find_fringe(height, width):
    parent_lst = []
    for edge_idx in range(round(min(height, width)/2) if min(height, width) != 1 else 1):
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

def solve(matrix, addresses, height, width):
    new_matrix = [[0 for _ in range(width)] for _ in range(height)]
    for idx, address in enumerate(addresses):
        if idx % 2 == 0:
            new_address = address[-1:] + address[:-1]
        else:
            new_address = address[1:] + address[:1]

        for new, old in zip(new_address, address):
            new_matrix[old[0]][old[1]] = matrix[new[0]][new[1]]

    return new_matrix

addresses = find_fringe(height, width)
new_matrix = solve(matrix, addresses, height, width)
for row in new_matrix:
    print(row)
