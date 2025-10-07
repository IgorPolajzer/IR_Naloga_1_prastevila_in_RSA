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

def random(x, y, ro):
    m = pow(2, 32)
    a = 69069
    b = 0

    return normalized_lcg(x, y, m, a, b, ro, 1000000)
    #return x + (numbers[-1] % (y - x)), numbers
