import sys
def find_neighbors(image, address):  
    x = address[0]
    y = address[1]
    addresses = []
    if y > 0 and image[x][y-1] == '🟧':
        addresses.append((x, y-1))
    if y < len(image[0]) - 1 and image[x][y+1] == '🟧':
        addresses.append((x, y+1))
    if x > 0 and image[x-1][y] == '🟧':
        addresses.append((x-1, y))
    if x < len(image) - 1 and image[x+1][y] == '🟧':
        addresses.append((x+1, y))

    return addresses

def spread(image, point_input):
    Frontier = []
    Frontier.append(point_input)
    while len(Frontier) != 0:
        point = Frontier[-1]
        del Frontier[-1]

        addresses = find_neighbors(image, point)
        for addr in addresses:
            image[addr[0]][addr[1]] = '🟦'
            Frontier.append(addr)
            

def sol(image, m, n):
    count = 0
    for i in range(m):
        for j in range(n):
            if image[i][j] == '🟧':
                spread(image, (i, j))
                count += 1
    
    return count
"""
# Read input from stdin
all_inputs = sys.stdin.read().strip().split('\n')
start = 0
result = []
"""
all_inputs = ['15 20',
'🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟧🟧🟧',
'🟫🟫🟧🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟧🟧',
'🟫🟧🟧🟧🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫',
'🟫🟫🟧🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫',
'🟫🟫🟫🟫🟫🟫🟫🟫🟧🟧🟧🟫🟫🟫🟫🟫🟫🟫🟫🟫',
'🟫🟫🟫🟫🟫🟫🟫🟧🟧🟧🟧🟧🟫🟫🟫🟫🟫🟫🟫🟫',
'🟫🟫🟫🟫🟫🟫🟫🟫🟧🟧🟧🟫🟫🟫🟫🟫🟫🟫🟫🟫',
'🟫🟫🟫🟧🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟧🟧',
'🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟧🟧🟧',
'🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟧🟫',
'🟫🟫🟫🟫🟫🟫🟫🟫🟧🟧🟧🟫🟫🟫🟫🟫🟫🟫🟫🟫',
'🟫🟫🟫🟫🟫🟫🟫🟧🟧🟧🟧🟫🟫🟫🟫🟫🟫🟫🟫🟫',
'🟫🟫🟫🟫🟫🟫🟫🟫🟧🟧🟧🟫🟫🟫🟫🟫🟫🟫🟫🟫',
'🟫🟫🟫🟫🟫🟫🟫🟫🟧🟧🟧🟫🟫🟫🟫🟫🟫🟫🟫🟫',
'🟫🟫🟫🟫🟫🟫🟫🟧🟧🟧🟧🟧🟫🟫🟫🟫🟫🟫🟫🟫',
'1 10',
'🟫🟧🟫🟫🟫🟫🟫🟧🟫🟫']
start = 0
result = []
# Process each case
while start < len(all_inputs):
    # Extract dimensions (m, n)
    m, n = map(int, all_inputs[start].split())
    
    # Extract the image matrix
    image = [list(all_inputs[start + 1 + i]) for i in range(m)]

    # Update the start index
    start += m + 1

    result.append(sol(image, m, n))
    
for i in range(len(result)):
    print(f'Case {i+1}: {result[i]}')