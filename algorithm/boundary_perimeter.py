import sys

height, width = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(height):
    row = list(map(str, sys.stdin.readline().split()))
    matrix.append(row)
    
# Only upper and rightside    
def count_neighbors(matrix, address):
    x = address[0]
    y = address[1]
    count_nei = 0
    if y + 1 < len(matrix[0]):
        if matrix[x][y+1] == '1':
            count_nei += 1
    if x > 0:
        if matrix[x-1][y] == '1' and x > 0:
            count_nei += 1
    
    return count_nei
    
def solution(matrix, height, width):
    total_count = 0
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == '1':
                total_count += 4 - 2*count_neighbors(matrix, [i, j] )
    
    return total_count

sys.stdout.write(str(solution(matrix, height, width)))