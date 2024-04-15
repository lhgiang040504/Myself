n = int(input())

storage = []
for i in range(n):
    drone = list(map(int, input().split()))
    storage.append((int((drone[0]**2 + (drone[1])**2)**0.5), i + 1))

def sol(storage):
    storage.sort()
    for i in range(len(storage)):
        if i + 1 > storage[i][0]:
            print(-1)
            return
        
    for drone in storage:
        print(drone[1], end=" ")

sol(storage)