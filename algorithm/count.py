import sys
#all_inputs = list(map(str.strip, sys.stdin.readlines()))
all_inputs = ['78 32',
'3 4 6 9 12 15 16 19 20 21 23 26 27 29 31 34 35 36 39 40 42 43 46 49 52 54 55 56 58 59 62 64 65 67 69 70 72 74 75 77 79 82 83 85 87 90 93 96 99 102 105 107 110 113 115 117 119 122 124 125 128 131 134 137 138 139 140 142 145 147 148 149 150 152 153 156 157 160',
'3 59 16 78 67 56 44 13 11 81 74 15 0 34 47 62 72 26 29 19 52 22 86 51 91 84 65 75 2 7 38 42']

lst = all_inputs[1].split(" ")

check_lst = all_inputs[2].split(" ")

positions = {}
for i, num in enumerate(lst):
    positions[num] = i

result = []
for num in check_lst:
    result.append(True if positions.get(num, -1) != -1 else False)

sys.stdout.write(str(result.count(True)))
    