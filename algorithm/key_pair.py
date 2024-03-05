# Not divisible by any perfect square
"""def get_root(num, root):
    if (num ** (1/root)) == int(num ** (1/root)):
        return (num ** (1/root), 1)
    else:
        check_list = []
        for i in range(round((num/2)**(1/2)), 1, -1):
            check_list.append(i ** root)
        
        temp = 1
        for x in check_list:
            if num % x == 0:
                temp = x
                break
        return (temp ** (1/root), num // temp)


L = int(input()) 
R = int(input()) 

count = 0
for i in range(L, R):
    for j in range(i + 1, R+1):
        temp = get_root(i*j, 2)
        if temp[0] == 1:
            count += 1

print(count)"""
from  math import gcd
limit = 10000
primes = []
def sieve_of_eratosthenes(primes, limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    # Iterate from 2 to square root of the limit.
    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            # Start at num*num to reduce the redundant acts.
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
    return primes
primes = sieve_of_eratosthenes(primes, limit)

l, r = map(int, input().split())
potential = []
# Composite number's prime factorization
for i in range(l, r + 1):
    check = True
    # With silver prime factors not 1
    for prime in primes:
        if i % (prime * prime) == 0:
            check = False
            break
        if i <= prime ** 2:
            break
    # Get filter numbers
    if check:
        potential.append(i)

count = 0
length = len(potential)
for i in range(length - 1):
    for j in range(i + 1, length):
        if gcd(potential[i], potential[j]) == 1:
            count += 1

print(count)