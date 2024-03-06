"""import math

def dist(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
def find_remaining_vertex(A, B, C):
    AB = (B[0] - A[0], B[1] - A[1])
    AC = (C[0] - A[0], C[1] - A[1])
    AD = (AB[0] + AC[0], AB[1] + AC[1])
    D = [A[0] + AD[0], A[1] + AD[1]]
    return D

A = list(map(int, input().split()))
B = list(map(int, input().split()))


x = a - x1
y = b - y1

squares = []
distance = int(dist(A, B))
a = B[0] - A[0]
b = B[1] - A[1]
if a == 0:
    C1 = [distance + A[0], A[1]]
    C2 = [-distance + A[0], A[1]]
elif b == 0:
    C1 = [A[0], distance + A[1]]
    C2 = [A[0], -distance + A[1]]
else:
    temp = distance**2 / (1 + (a/b)**2)
    C1 = [int(temp**0.5 + A[0]), int(-a * temp / b + A[1])]
    C2 = [int(-temp**0.5 + A[0]), int(-a * -temp / b + A[1])]

squares.append([A, B, find_remaining_vertex(A, B, C1), C1])
squares.append([A, B, find_remaining_vertex(A, B, C2), C2])
    
for i in range(2):
    if i == 0:
        squares[i] = [squares[i][0]] + squares[i][:0:-1]

    print((squares[i][0][0],squares[i][0][1]),(squares[i][1][0],squares[i][1][1]),(squares[i][2][0],squares[i][2][1]),(squares[i][3][0],squares[i][3][1]))"""

def find_remaining_vertices(A, B): 
    x3 = A[0] + (B[1] - A[1])
    y3 = A[1] - (B[0] - A[0])
    C1 = (x3, y3)

    x4 = B[0] + (B[1] - A[1])
    y4 = B[1] - (B[0] - A[0])
    D1 = (x4, y4)

    x3 = A[0] - (B[1] - A[1])
    y3 = A[1] + (B[0] - A[0])
    C2 = (x3, y3)

    x4 = B[0] - (B[1] - A[1])
    y4 = B[1] + (B[0] - A[0])
    D2 = (x4, y4)
    return ((A, C2, D2, B),(A, B, D1, C1))

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
res = find_remaining_vertices(A, B)
for case in res:
    print(case[0],case[1],case[2],case[3])