from math import sqrt, gcd

import numpy as np

NUMBERS_COUNT = 100


def lcg(m, a, b, ro, size):
    r = np.zeros(size, dtype=np.uint64)
    r[0] = ro

    for i in range(1, size):
        r[i] = (a * r[i - 1] + b) % m

    return r


def random(x, y, ro, size=1000000):
    # Super-Duper parameters.
    m = pow(2, 32)
    a = 69069
    b = 0

    numbers = lcg(m, a, b, ro, size)

    # Vectorized Normalization.
    numbers = x + (numbers % (y - x + 1))

    return numbers


def naive_test(p):
    if p < 2:
        return p, "COMPOSITE"
    if p == 2:
        return p, "PRIME"
    if p % 2 == 0:
        return p, "COMPOSITE"

    j = 3
    while j <= sqrt(p):
        if p % j == 0:
            break

        j += 2

    if j > sqrt(p):
        return p, "PRIME"
    else:
        return p, "COMPOSITE"


def generate_prime_naive(n):
    # Calculate the maximum value for an n-bit number
    max_value = pow(2, n) - 1

    # Generate random number.
    p = random(0, max_value, 1, NUMBERS_COUNT)[-1]

    if p % 2 == 0:
        p += 1

    while True:

        p, result = naive_test(p)

        if result == "PRIME":
            return int(p)

        p += 2


def miller_rabin_test(p, s, ro):
    if p <= 3:
        return "PRIME"
    if p % 2 == 0:
        return "COMPOSITE"

    d = p - 1
    k = 0
    while d % 2 == 0:
        d //= 2
        k += 1

    seed = ro
    for i in range(s):
        a = random(2, p - 2, seed, NUMBERS_COUNT)[-1]
        x = pow(int(a), int(d), int(p))  # modular_exponentiation(int(a), int(d), int(p))

        if x == 1 or x == p - 1:
            seed += 1
            continue

        for _ in range(k - 1):
            x = (x * x) % p
            if x == p - 1:
                break
        else:
            return "COMPOSITE"

        seed += 1

    return "PROBABLY_PRIME"


def generate_prime_miller_rabin_bitsize(n, s, ro=1):
    # Calculate the maximum value for an n-bit number
    max_value = pow(2, n) - 1

    # Generate random number.
    p = random(0, max_value, ro, NUMBERS_COUNT)[-1]

    if p % 2 == 0:
        p += 1

    while True:
        output = miller_rabin_test(p, s, ro)
        if output == "PRIME" or output == "PROBABLY_PRIME":
            return int(p)

        p += 2


def generate_prime_miller_rabin_interval(s, min, max, ro=1):
    # Generate random number.
    p = random(min, max, ro, NUMBERS_COUNT)[-1]

    if p % 2 == 0:
        p += 1

    while True:
        output = miller_rabin_test(p, s, ro)
        if output == "PRIME" or output == "PROBABLY_PRIME":
            return int(p)

        p += 2


def modular_exponentiation(a, b, n):
    d = 1
    bodi = int_to_binary_array(b)  # Convert b to binary array

    # Iterate from the most significant bit to the least significant bit
    for i in range(len(bodi), -1):
        d = (d * d) % n
        if bodi[i - 1] == 1:
            d = (d * a) % n

    return d


def int_to_binary_array(integer: int) -> list:
    integer = int(integer)
    # Convert to binary and remove the '0b' prefix
    binary_string = bin(integer)[2:]

    # Use list comprehension to create the bit array
    return [int(bit) for bit in binary_string]


def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclid(b, a % b)

        # n_d, n_x, n_y.
        return d, y, x - (a // b) * y


def modular_linear_equation_solver(a, b, n):
    d, x, y = extended_euclid(a, n)

    if b % d == 0:
        xo = (x * (b // d)) % n

        solutions = []
        for i in range(d):
            solution = (xo + i * (n // d)) % n
            solutions.append(solution)

        return solutions
    else:
        return None


def generate_and_store_key(n, file_path):
    p = None
    q = None

    # 1. Step.
    seed = 1
    while p == q:
        p = generate_prime_miller_rabin_bitsize(n, 10, seed)
        seed += 1
        q = generate_prime_miller_rabin_bitsize(n, 10, seed)
        seed += 1

    # 2. Step.
    n = p * q
    euler = (p - 1) * (q - 1)

    # 3. Step.
    e = generate_prime_miller_rabin_interval(1, euler, seed)
    seed += 1

    while gcd(e, euler) > 1:
        e = generate_prime_miller_rabin_interval(1, euler, seed)
        seed += 1

    # 4. Step.
    print(modular_linear_equation_solver(e, 1, euler))
