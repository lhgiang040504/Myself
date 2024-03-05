def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    # Because any composite number's prime factorization will have at least one prime factor less than or equal to its square root
    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            # The reason for using num * num instead of num + num is to optimize the algorithm and avoid redundant work.
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

print(sieve_of_eratosthenes(1000))