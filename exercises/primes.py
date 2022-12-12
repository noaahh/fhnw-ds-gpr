import time


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True

for i in range(1, 5):
    print(is_prime(i))

print(is_prime(47))


def all_primes(n):
    return [x for x in range(2, n) if is_prime(x)]

print(all_primes(100))

def eratosthenes(n):
    not_primes = {}
    primes = []

    for x in range(2, n + 1):
        if x not in not_primes.keys():
            primes.append(x)

            for i in range(x + 1, n + 1):
                if i % x == 0:
                    not_primes[i] = 1

    return primes

print(eratosthenes(100))

def distances(primes):
    return [primes[i] - primes[i - 1] for i in range(1, len(primes))]

print(distances(eratosthenes(100)))

def heuristic(distances):
    return [(i, distances.count(i)) for i in range(0, max(distances) + 1) if distances.count(i) != 0]

print(heuristic(distances(eratosthenes(100))))
