def can_transform(a, b):
    if len(a) != len(b):
        return 'NO'
    
    oddidx_element_a = []
    evenidx_element_a = []
    oddidx_element_b = []
    evenidx_element_b = []
    i = 0
    for x, y in zip(a, b):
        if i % 2 == 0:
            evenidx_element_a.append(x)
            evenidx_element_b.append(y)
        else:
            oddidx_element_a.append(x)
            oddidx_element_b.append(y)
        i += 1
        
    if sorted(evenidx_element_a) != sorted(evenidx_element_b) or \
       sorted(oddidx_element_a) != sorted(oddidx_element_b):
        return 'NO'
    
    return 'YES'

n = int(input())
results = []
for i in range(n):
  a = input()
  b = input()
  results.append(can_transform(a, b))

for result in results:
    print(result)