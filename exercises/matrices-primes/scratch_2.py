def well_formed_matrix(m):
    prev_len = None

    if len(m) == 0:
        return False

    for i in range(len(m)):
        m_i = m[i]
        if len(m_i) == 0 or (i > 0 and len(m_i) != prev_len):
            return False

        prev_len = len(m_i)

    return True


def transpose(m):
    if not well_formed_matrix(m):
        raise ValueError("m is not a well-formed matrix")

    t = []
    for i in range(len(m[0])):
        r = []
        for row in m:
            r.append(row[i])

        t.append(r)

    return t


def eratosthenes_fast(n):
    not_primes = {}
    primes = []

    for x in range(2, n + 1):
        if x not in not_primes.keys():
            primes.append(x)

            for i in range(x + 1, n + 1):
                if i % x == 0:
                    not_primes[i] = 1

    return primes


def eratosthenes(n):
    not_primes = []
    primes = []

    for x in range(2, n + 1):
        if x not in not_primes:
            primes.append(x)
            for i in range(x + 1, n + 1):
                if i % x == 0:
                    not_primes.append(i)

    return primes


def eratosthenes_wolf(n):
    sieve = [False] * (n + 1)  # sieve[i] bedeutet: i ist durchgestrichen
    i = 2
    while i < n + 1:
        if not sieve[i]:
            j = 2
            while i * j < n + 1:
                sieve[i * j] = True
                j += 1
        i += 1
    res = []
    for i in range(2, n + 1):
        if not sieve[i]:
            res.append(i)
    return res

print(eratosthenes_wolf(100000))
print(eratosthenes_fast(100000))
