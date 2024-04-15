max = float('inf')


'''n = int(input())
adj = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj.append(row)
'''
adj = [[0, 10, 15, 20],
       [10, 0, 35, 25],
       [15, 35, 0, 30],
       [20, 25, 30, 0]]
n = 4

class TSP():
    def __init__(self, adj, n):
        self.adjacency = adj
        self.n = n
        self.visited = [False] * n
        self.final_path = [-1] * (n + 1)
        self.curr_path = [-1] * (n + 1)
        self.min_bound = float('inf')

    def firstMin(self, i):
        min = float('inf')
        for j in range(self.n):
            if self.adjacency[i][j] < min and self.adjacency[i][j] != 0:
                min = self.adjacency[i][j]
        return min

    def secondMin(self, i):
        fMin = float('inf')
        sMin = float('inf')
        for j in range(self.n):
            if self.adjacency[i][j] == 0:
                continue

            if self.adjacency[i][j] < fMin:
                sMin = fMin
                fMin = self.adjacency[i][j]
            elif self.adjacency[i][j] < sMin  and self.adjacency[i][j] != fMin:
                sMin = self.adjacency[i][j]
        return sMin
    
    def sol(self, level, bound, weight):
        if level == self.n:
            if adj[self.curr_path[level - 1]][self.curr_path[0]] != 0:
                total_weight = weight + adj[self.curr_path[level - 1]][self.curr_path[0]]

                if total_weight < self.min_bound:
                    self.final_path[:] = self.curr_path[:]
                    self.min_bound = total_weight

            return

        for i in range(self.n):
            if not self.visited[i] and adj[self.curr_path[level - 1]][i] != 0:
                temp_b = bound
                temp_w = weight
                weight += adj[self.curr_path[level - 1]][i]
            
                if level == 1:
                    bound -= ((self.firstMin(self.curr_path[level - 1]) + self.firstMin(i)) // 2)
                else:
                    bound -= ((self.secondMin(self.curr_path[level - 1]) + self.firstMin(i)) // 2)
                if bound + weight < self.min_bound:
                    self.curr_path[level] = i
                    self.visited[i] = True
                    self.sol(level + 1, bound, weight)
                
                weight = temp_w
                bound = temp_b
                self.visited[i] = False
                self.curr_path[level] = -1

    def solve(self):
        bound = 0
        for i in range(self.n):
            bound += (self.firstMin(i) + self.secondMin(i))
        bound = bound // 2
        
        self.curr_path[-1] = 0
        self.curr_path[0] = 0
        self.visited[0] = True
        self.sol(1, bound, 0)

solver = TSP(adj, n)
solver.solve()

for city in solver.final_path:
    print(city, end=' ')

