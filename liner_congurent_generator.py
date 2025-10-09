def lcg(m, a, b, ro, size) -> list:
    r = [None] * size

    r[0] = ro

    # Generate the sequence
    for i in range(0, size - 1):
        r[i + 1] = (a * r[i] + b) % m

    return r


def random(x, y, ro):
    m = pow(2, 32) - 1
    a = 69069
    b = 0

    numbers = lcg(m, a, b, ro, 1000000)

    for i in range(0, len(numbers)):
        numbers[i] = x + numbers[i] % (y - x + 1)

    return numbers
