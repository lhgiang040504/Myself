def quick_power_recursive(a, x):
    print(a, x)
    
    result = 1
    if x == 0:
        return 1
    elif x % 2 == 1:
        result *= a

    temp = quick_power_recursive(a, x // 2)
    return result * temp * temp

def quick_power_iterative(a, x):
    result = 1
    core = a
    while x > 1:
        if x % 2 == 1:
            result *= core
            x -= 1
        x //= 2
        core *= core
        print(result, core)

    return result * core

print(quick_power_iterative(5, 3))