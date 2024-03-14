import sys
#all_inputs = list(map(str, sys.stdin.readlines()))
all_inputs = ['7',
'0 0',
'1 0',
'1 1',
'2 1',
'2 0',
'3 0',
'3 -1']
list_points = []
n = int(all_inputs[0])
count = 0
for i in range(1, n + 1):
    point = all_inputs[i].split()
    # Point C
    list_points.append((int(point[0]), int(point[1])))
    
    if len(list_points) < 3:
        continue

    prefisrt_point = list_points[-2] # Point B
    presecond_point = list_points[-3] # Point A

    if presecond_point[1] == prefisrt_point[1] + 1:
        if presecond_point[0] == int(point[0]) + 1:
            count += 1
    elif presecond_point[1] == prefisrt_point[1] - 1:
        if presecond_point[0] == int(point[0]) - 1:
            count += 1
    elif presecond_point[0] == prefisrt_point[0] + 1:
        if presecond_point[1] == int(point[1]) - 1:
            count += 1
    elif presecond_point[0] == prefisrt_point[0] - 1:
        if presecond_point[1] == int(point[1]) + 1:
            count += 1

sys.stdout.write(str(count))