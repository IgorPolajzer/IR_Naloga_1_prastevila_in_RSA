from math import sqrt


def lcg(m, a, b, ro, size) -> list:
    r = [None] * size

    r[0] = ro

    # Generate the sequence
    for i in range(0, size - 1):
        r[i + 1] = (a * r[i] + b) % m

    return r


def random(x, y, ro):
    # Super-Duper parameters.
    m = pow(2, 32)
    a = 69069
    b = 0

    numbers = lcg(m, a, b, ro, 1000000)

    # Normalization.
    for i in range(0, len(numbers)):
        numbers[i] = x + numbers[i] % (y - x + 1)

    return numbers


def naive_test(p):
    j = 3
    while j <= sqrt(p):
        if p % j == 0:
            break

        j += 2

    if j > sqrt(p):
        return p, "PRIME"
    else :
        return p, "COMPOSITE"


def generate_prime_naive(n):
    # Calculate the maximum value for an n-bit number
    max_value = pow(2, n) - 1

    # Generate random number.
    p = random(0, max_value, 1)[-1]

    if p % 2 == 0:
        p += 1

    while True:

        p, result = naive_test(p)

        if result == "PRIME":
            return p

        p += 2


def miller_rabin_test(p, s):
    if p <= 3:
        return "PRIME"
    if p % 2 == 0:
        return "COMPOSITE"

    d = p - 1
    k = 0
    while d % 2 == 0:
        d //= 2
        k += 1

    for _ in range(s):
        a = random(2, p - 2, 1)[-1]
        x = modular_exponentiation(a, d, p)

        if x == 1 or x == p - 1:
            continue

        for _ in range(k - 1):
            x = (x * x) % p
            if x == p - 1:
                break
        else:
            return "COMPOSITE"

    return "PROBABLY_PRIME"


def generate_prime_miller_rabin(n, s):
    # Calculate the maximum value for an n-bit number
    max_value = pow(2, n) - 1

    # Generate random number.
    p = random(0, max_value, 1)[-1]

    if p % 2 == 0:
        p += 1

    while True:
        j = 3

        output = miller_rabin_test(p, s)
        if output == "PRIME" or output == "PROBABLY_PRIME":
            return p

        p += 2


def modular_exponentiation(a, b, n):
    d = 1
    bodi = int_to_binary_array(b)  # Convert b to binary array

    # Iterate from the most significant bit to the least significant bit
    for i in range(len(bodi), 0):
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
