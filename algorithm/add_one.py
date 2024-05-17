def perform_transformations(num, n):
    for _ in range(n):
        num = ''.join(str(int(d) + 1) for d in num)
    return len(num)

def perform_transformations(num, n, memo={}):
    if (num, n) in memo:
        return memo[(num, n)]

    if n == 0:
        memo[(num, n)] = len(num)
        return memo[(num, n)]

    transformed_num = ''.join(str(int(d) + 1) for d in num)
    memo[(num, n)] = perform_transformations(transformed_num, n - 1, memo)
    return memo[(num, n)]

'''num_testcase = int(input())
result = []'''
num_testcase = 5
inputs =   [['1912', '1'],
            ['5', '6'],
            ['999', '1'],
            ['88', '2'],
            ['12', '100']]
result = []
for i in range(num_testcase):
    #num, n = input().split()
    num, n = inputs[i]
    result.append(perform_transformations(num, int(n)))

for res in result:
    print(res)