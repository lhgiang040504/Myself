#heights = list(map(int, input().split()))
heights = [6, 2, 5, 4, 5, 1, 6]
heights.append(-1)

stack = []
stack.append((0, 0))
max_area = 0
for idx, height in enumerate(heights):
    new_idx = idx
    while len(stack) != 0:
        if height > stack[-1][1]:
            stack.append((new_idx, height))
            break
        else:
            curr = stack[-1]
            stack.pop()
            new_idx = curr[0]
            temp = (idx - curr[0]) * curr[1]
            if temp > max_area:
                max_area = temp

print(max_area)