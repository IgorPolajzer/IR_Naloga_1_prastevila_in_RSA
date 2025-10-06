import numpy as np

#Ri+1=aRi+b (mod m),
def lcg(m, a, b, ro) -> list:
    size = 10000
    r = np.zeros(size)

    r[0] = ro

    # Generate the sequence
    for i in range(1, size):
        r[i] = (a * r[i - 1] + b) % m

    return r

# 8 bit number generator
def random():
    x = pow(2, 7)
    y = pow(2, 8) - 1

    return x + lcg(pow(2, 32), 69069, 0, 1).pop() % (y - x + 1)
