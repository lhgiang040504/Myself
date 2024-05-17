rows, cols = map(int, input().split())

matrix = []
for _ in range(rows):
    row = input().split()
    matrix.append(row)

histogram = [0] * cols
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == '1':
            histogram[j] += 1
  
def max_area_histogram(histogram): 
    stack = list() 
  
    max_area = 0

    index = 0
    while index < len(histogram): 
        if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
            stack.append(index) 
            index += 1
        else: 
            top_of_stack = stack.pop() 

            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1) 
                     if stack else index)) 
  
            max_area = max(max_area, area) 

    while stack: 
        top_of_stack = stack.pop() 

        area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1) 
                 if stack else index)) 
  
        max_area = max(max_area, area) 
    return max_area 

print(max_area_histogram(histogram))