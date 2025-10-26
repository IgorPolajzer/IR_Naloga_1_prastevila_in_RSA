from math import sqrt, gcd, log, ceil, floor

import numpy as np

from util import *

NUMBERS_COUNT = 100
PUBLIC_KEY_FILE_NAME = r"\privkey.txt"
PRIVATE_KEY_FILE_NAME = r"\pubkey.txt"
seed = 1
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


def is_prime_naive(p):
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


def generate_prime_naive_method(n, ro=1):
    # Calculate the maximum value for an n-bit number
    max_value = pow(2, n) - 1

    # Generate random number.
    p = random(0, max_value, ro, NUMBERS_COUNT)[-1]

    if p % 2 == 0:
        p += 1

    while True:

        p, result = is_prime_naive(p)

        if result == "PRIME":
            return int(p)

        p += 2


def is_prime_miller_rabin(p, s, ro):
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
        x = pow(int(a), int(d), int(p))  # modular_exponantion(int(a), int(d), int(p))

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


def generate_prime_miller_rabin(n, s, ro=1):
    # Calculate the maximum value for an n-bit number
    max_value = pow(2, n) - 1

    # Generate random number.
    p = random(0, max_value, ro, NUMBERS_COUNT)[-1]

    if p % 2 == 0:
        p += 1

    while True:
        output = is_prime_miller_rabin(p, s, ro)
        if output == "PRIME" or output == "PROBABLY_PRIME":
            return int(p)

        p += 2


def generate_prime_in_interval(s, min, max, ro=1):
    # Generate random number.
    p = random(min, max, ro, NUMBERS_COUNT)[-1]

    if p % 2 == 0:
        p += 1

    while True:
        output = is_prime_miller_rabin(p, s, ro)
        if output == "PRIME" or output == "PROBABLY_PRIME":
            return int(p)

        p += 2


def generate_rsa_key_pair(n, algorithm: Algorithm):
    global seed
    p = None
    q = None

    while p == q:
        if algorithm == Algorithm.NAIVE:
            p = generate_prime_naive_method(n, seed)
            seed += 1
            q = generate_prime_naive_method(n, seed)
            seed += 1

        elif algorithm == Algorithm.MILLER_RABIN:
            p = generate_prime_miller_rabin(n, 10, seed)
            seed += 1
            q = generate_prime_miller_rabin(n, 10, seed)
            seed += 1

    return p, q


def store_rsa_keys(n, file_path, algorithm: Algorithm):
    global seed

    # 1. Step.
    p, q = generate_rsa_key_pair(n, algorithm)

    # 2. Step.
    n = p * q
    euler = (p - 1) * (q - 1)

    # 3. Step.
    e = generate_prime_in_interval(1, euler, seed)
    seed += 1

    while gcd(e, euler) > 1:
        e = generate_prime_in_interval(1, euler, seed)
        seed += 1

    # 4. Step.
    d = modular_linear_equation_solver(e, 1, euler)[-1]

    if d is None:
        print("Modular linear equation solver couldnt find the result.")
        return

    # 5. Step.
    p_key = e, n
    s_key = d, n

    write_key_to_file(p_key, file_path + PUBLIC_KEY_FILE_NAME)
    write_key_to_file(s_key, file_path + PRIVATE_KEY_FILE_NAME)


def rsa_encrypt_file(file_path, key_path):
    p_key = read_key_from_file(key_path + PUBLIC_KEY_FILE_NAME)
    encrypt_and_write_file(file_path, p_key)


def rsa_decrypt_file(file_path, key_path):
    s_key = read_key_from_file(key_path + PRIVATE_KEY_FILE_NAME)
    decrypt_and_write_file(file_path, s_key)
