n = 9

storage = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

localMax = storage[0]
globalMax = storage[0]

globalstart = 0
start = 0
end = 0

for i in range(1, n):
    if storage[i] > localMax + storage[i]:
        localMax = storage[i]
        start = i
    else:
        localMax += storage[i]

    if  globalMax < localMax:
        globalMax = localMax
        end = i
        globalstart = start

print(globalMax)