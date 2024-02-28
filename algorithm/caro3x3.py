def get_diagonals_and_lines(matrix):
    return [
      # Đường chéo chính
      [matrix[i][i] for i in range(3)],
      # Đường chéo phụ
      [matrix[i][2-i] for i in range(3)],
      # Các đường thẳng
      *[matrix[i] for i in range(3)],
      *[list(col) for col in zip(*matrix)],
    ]

def solve(matrix, lst):
    check_lst = get_diagonals_and_lines(matrix)
        
    for case in check_lst:
        if all(element in lst for element in case):
            return 'Yes'
    return 'No'


matrix = []
for _ in range(3):
    row = input("Nhập dòng {}: ".format(_ + 1)).split()
    matrix.append(row)

lst = []
n = int(input())
for _ in range(n):
    num = input()
    lst.append(num)

print(solve(matrix, lst))
