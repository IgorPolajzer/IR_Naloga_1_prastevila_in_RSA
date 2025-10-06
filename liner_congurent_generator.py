def normalized_lcg(x, y, m, a, b, ro, size) -> list:
    r = [0] * size

    r[0] = ro

    # Generate the sequence
    for i in range(1, size):
        r[i] = x + ((a * r[i - 1] + b) % m) % (y - x + 1)

    return r
def lcg(m, a, b, ro, size) -> list:
    r = [0] * size

    r[0] = ro

    # Generate the sequence
    for i in range(1, size):
        r[i] = (a * r[i - 1] + b) % m

    return r

def random(ro):
    x = pow(2, 7)
    y = pow(2, 8) - 1

    return x + lcg(pow(2, 32), 69069, 0, ro, 10000)[-1] % (y - x + 1)
