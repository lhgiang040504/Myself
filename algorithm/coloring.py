n = int(input())
adjacency = []
for i in range(n):
    row = input().split()
    adjacency.append(row)
            

def solve(adjacency, n):
    nation_colors = [-1] * n

    nation_colors[0] = 0
    
    for i in range(1, n):
        used_colors = []
        for j in range(n):
            if adjacency[i][j] == '1' and nation_colors[j] != -1:
                used_colors.append(nation_colors[j])
                    
        min_color = 0
        while min_color in used_colors:
            min_color += 1

        nation_colors[i] = min_color
    
    return len(set(nation_colors))

print(solve(adjacency, n))