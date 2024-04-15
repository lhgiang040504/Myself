a = input()
b = input()

def check_equivalent(a, b):
    if a == b:
        return True
    if len(a) != len(b) or len(a) % 2 != 0:
        return False
    
    length = len(a) // 2
    a1, a2 = a[:length], a[length:]
    b1, b2 = b[:length], b[length:]
    
    return (check_equivalent(a1, b1) and check_equivalent(a2, b2)) or (check_equivalent(a1, b2) and check_equivalent(a2, b1))
    
if not check_equivalent(a, b):
    print("NO")
else:
    print("YES")