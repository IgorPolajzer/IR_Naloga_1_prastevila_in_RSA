def modular_exponentiation(a, b, n) -> int:
    d = 1
    bodi = int_to_binary_array(b)  # Convert b to binary array

    # Iterate from the most significant bit to the least significant bit
    for i in range(len(bodi), -1):
        d = (d * d) % n
        if bodi[i - 1] == 1:
            d = (d * a) % n

    return d


def big_modular_exponantion(a, b, n) -> int:
    d = 1
    bodi = int_to_binary_array(b)

    for i in range(len(bodi) - 1, 0, -1):
        d = pow(d, 2) % n

        if bodi[i] == 1:
            d = (d * a) % n

    return d


def int_to_binary_array(integer: int) -> list:
    integer = int(integer)
    # Convert to binary and remove the '0b' prefix
    binary_string = bin(integer)[2:]

    # Use list comprehension to create the bit array
    return [int(bit) for bit in binary_string]


def positive_mod(a, b):
    if a < 0:
        return a + b

    return a % b


def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclid(b, positive_mod(a, b))

        # n_d, n_x, n_y.
        return d, y, x - (a // b) * y


def modular_linear_equation_solver(a, b, n) -> list | None:
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


def write_key_to_file(key: tuple, file_path: str):
    with open(file_path, 'w') as file:
        for element in key:
            file.write(f"{element}\n")


def read_key_from_file(file_path: str) -> tuple:
    with open(file_path, 'r') as file:
        elements = file.readlines()
    return tuple(int(element.strip()) for element in elements)


class Algorithm:
    NAIVE = 1
    MILLER_RABIN = 2
