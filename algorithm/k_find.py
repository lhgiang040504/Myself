import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
nums = list(map(str, sys.stdin.readline().split()))

def k_find(n, lst, k, x):
    start = 0
    end = n - 1
    
    while end - start + 1 > k:
        if abs(lst[end] - x) > abs(lst[start] - x):
            end -= 1
        else:
            start += 1
    
    return lst[start:end+1]

result = k_find(n, lst, int(nums[0]), int(nums[1]))
sys.stdout.write(" ".join(map(str, result)) + '\n')

import sys
#all_inputs = sys.stdin.readlines()
all_inputs = ['21',
'26475 26477 26479 26481 26481 26483 26483 26484 26485 26487 26489 26489 26490 26491 26492 26492 26493 26493 26494 26495 26496',
'3 32272',
'4 27892',
'9 18564',
'10 15216',
'4 15714',
'20 256',
'11 38574',
'']
n = int(all_inputs[0].strip())
lst = list(map(int, all_inputs[1].strip().split()))

def k_find_optimized(n, lst, k, x):
    if x >= lst[-1]:
        return [lst[n - k], lst[-1]]
    else:
        return [lst[0], lst[k - 1]]

    """# Insertion index for x 
    low = 0
    high = n - 1
    while True:
        mid = (low + high) // 2
        if (lst[mid] <= x and lst[mid + 1] > x) :
            low = mid
            break
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    high = low
    count = 0
    while low >= 0 and high < n and count < k:
        if (x - lst[low] <= lst[high] - x):
            low -= 1
        else:
            high += 1
        count += 1
    while count < k and low >= 0:
        low -= 1
        count += 1
    while count < k and high < n:
        high += 1
        count += 1
    
    return [lst[low], lst[high]]"""

def find_k_closest_elements(n, nums, k, target):
    left = 0
    right = n - 1
 
    while right - left >= k:
        # Compare the absolute differences between the target and elements at left and right pointers
        if abs(nums[left] - target) > abs(nums[right] - target):
            left += 1
        else:
            right -= 1
 
    # Print the `k` closest elements
    return (nums[left], nums[right])

import heapq
def findClosestElements(n, arr, k, x):
    max_heap = []
 
    for num in arr:
        if num == x:
            continue
 
        diff = abs(num - x)
        heapq.heappush(max_heap, (-diff, num))
 
        if len(max_heap) > k:
            heapq.heappop(max_heap)
 
    result = []
 
    while max_heap:
        diff, num = heapq.heappop(max_heap)
 
        result.append(num)
    result.sort()
    return (result[0], result[-1])

def findClosestElements(n, arr, k, x):
    left, right = 0, len(arr) - k

    while left < right:
        mid = (left + right) // 2
    
        if x - arr[mid] <= arr[mid + k] - x:
            right = mid
        else:
            left = mid + 1
      
    return (arr[left], arr[left + k - 1])

result = []
i = 2
while True:
    if all_inputs[i].strip() == '':
        break
    k, x = map(int, all_inputs[i].split())
    result.append(findClosestElements(n, lst, k, x))
    i += 1

for r in result:
    sys.stdout.write(" ".join(map(str, r)) + '\n')