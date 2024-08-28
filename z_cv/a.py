import numpy as np
def rotate(arr, edge_idx):
    if edge_idx % 2 == 0:
        arr_fringed = np.concatenate((arr[-1:], arr[:-1]), axis=0)
    else:
        arr_fringed = np.concatenate((arr[1:], arr[:1]), axis=0)
    return arr_fringed
def separate(matrix, edge_idx):
    # Upper row
    upper_r = matrix[edge_idx, edge_idx:W - edge_idx - 1]
    # Right column
    right_c = matrix[edge_idx:H - edge_idx - 1, W - edge_idx]
    # Lower row
    lower_r = matrix[H - edge_idx, edge_idx:W - edge_idx - 1]
    lower_r = lower_r[::-1]
    # Left column
    left_c = matrix[edge_idx:H - edge_idx - 1,edge_idx]
    left_c = left_c[::-1]

    cicle = np.concatenate((upper_r, right_c, lower_r, left_c), axis=0)
    return cicle

def combine(matrix, circle, edge_idx):
    matrix[edge_idx, edge_idx:W - edge_idx - 1] = circle[:W - 2 * edge_idx - 1]
    matrix[edge_idx:H - edge_idx - 1, W - edge_idx] = circle[W - 2 * edge_idx - 1:2 * (W - 2 * edge_idx - 1)]
    matrix[H - edge_idx, edge_idx:W - edge_idx - 1] = circle[2 * (W - 2 * edge_idx - 1):3 * (W - 2 * edge_idx - 1)]
    matrix[edge_idx:H - edge_idx - 1, edge_idx] = circle[3 * (W - 2 * edge_idx - 1):]
    return matrix
    

def rotate_edge(matrix):
    for edge_idx in range(min(H, W) // 2 + 1):
        cicle = separate(matrix, edge_idx)
        circle_rotated = rotate(cicle, edge_idx)
        matrix = combine(matrix, circle_rotated, edge_idx)

    return matrix
        
# Ví dụ

matrix = np.array(matrix)
rotated_arr = rotate_edge(matrix)
print(rotated_arr)

