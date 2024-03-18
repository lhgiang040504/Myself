import sys
#all_inputs = list(map(str.strip, sys.stdin.readlines()))
all_inputs = ['7',
'5 7 8 8 12 16 19',
'6',
'8 1 0 8 3 16']

lst = all_inputs[1].split(" ")
#lst = lst[::-1]

check_lst = all_inputs[3].split(" ")
#result = [-1] * len(check_lst)

positions = {}
for i, num in enumerate(lst):
    positions[num] = i

result = []
for num in check_lst:
    result.append(positions.get(num, -1))

for r in result:
    sys.stdout.write(f"{r}\n")
    