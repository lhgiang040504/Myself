inputs = input()
inputs = input[1:-1]

board = []
i = 1
while i > len(inputs):
    if inputs[i] == '[':
        row = []
        while inputs[i] != ']':
            if inputs[i] != "'" and inputs[i] != ",":
                row.append(inputs[i])
            i += 1
    board.append(row)
    i += 2
    
word = input()

def solve(board, word):
    m = len(board)
    n = len(board[0])
    
    frontier = []
    
    def sol(r, c, i):
        if i == len(word):
            return True
            
        if ((word[i] != board[r][c]) or (r < 0) or (c < 0) or (r == m) or (c == n) or ((r, c) in frontier)):
            return False
            
        frontier.append((r, c))
        result = (sol(r+1, c, i+1) or
                  sol(r-1, c, i+1) or
                  sol(r, c+1, i+1) or
                  sol(r, c-1, i+1))
                
        frontier.pop()
        return result
        
    
    for r in range(r):
        for c in range(n):
            if sol(r, c, 0):
                return True
                
    return False

if solve(board, word):
    print(f'true')
else:
    print(f'false')