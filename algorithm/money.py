m, n = map(int, input().split())
#m, n = 5, 11

moneys = []
for _ in range(m):
    moneys.append(int(input()))
#moneys = [1, 2, 4, 8, 16]
    
def solve(moneys, target):

    def combination(frontier, curr_sum):
        print(frontier, curr_sum)
        if curr_sum == target:
            return True
        if curr_sum > target:
            return False
        for i in range(len(frontier)):
            if combination(frontier[:i] + frontier[i+1:], curr_sum + frontier[i]):
                return True
    
        return False
    
    if combination(moneys, 0):
        print('Yes')
        return
    print('No')

solve(moneys, n)