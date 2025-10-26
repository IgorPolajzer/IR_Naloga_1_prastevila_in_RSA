from math import ceil, log, floor


def modular_exponentiation(a, b, n) -> int:
    d = 1
    bodi = int_to_binary_array(b)  # Convert b to binary array

    # Iterate from the most significant bit to the least significant bit
    for i in range(len(bodi), 0, -1):
        d = (d * d) % n
        if bodi[i - 1] == 1:
            d = (d * a) % n

    return d


def big_modular_exponantion(a, b, n) -> int:
    d = 1
    bodi = int_to_binary_array(b)

    for i in range(len(bodi), 0, -1):
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


def read_file_in_binary(file_path: str, bits) -> list:
    # chunks = []
    # with open(file_path, 'rb') as f:
    #     return f.read()

    chunks = []
    bit_buffer = 0  # Buffer to store bits
    bits_in_buffer = 0  # Number of valid bits in buffer

    with open(file_path, 'rb') as f:
        while True:
            # Read bytes until we have enough bits.
            while bits_in_buffer < bits:
                byte = f.read(1)
                if not byte:
                    # End of file - handle remaining bits.
                    if bits_in_buffer > 0:
                        chunks.append(bit_buffer)
                    return chunks

                # Shift bits and add new byte.
                bit_buffer = (bit_buffer << 8) | byte[0]
                bits_in_buffer += 8

            # Shift bits by the needed remainder
            shift_amount = bits_in_buffer - bits
            chunk = (bit_buffer >> shift_amount) & ((1 << bits) - 1)
            chunks.append(chunk)

            # Update buffer: remove extracted bits
            bit_buffer &= (1 << shift_amount) - 1
            bits_in_buffer = shift_amount


class Algorithm:
    NAIVE = 1
    MILLER_RABIN = 2


def encrypt_and_write_file(file_path: str, p_key):
    e, n = p_key

    M = floor(log(n, 2))
    N = ceil(log(n, 2))

    chunks = read_file_in_binary(file_path, M)

    with open(
            r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\encryptet_files\enc.bin",
            "wb") as binary_file:
        for chunk in chunks:
            c = pow(chunk, e,
                    n)  # big_modular_exponantion(int(chunk), int(e),int(n))  # TODO Fix modular_exponentiation(int(a), int(d), int(p))
            binary_file.write(c.to_bytes(N, 'big'))


def decrypt_and_write_file(file_path: str, s_key):
    d, n = s_key
    N = ceil(log(n, 2))
    m_chunks = []

    with open(r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\encryptet_files\enc.bin","rb") as binary_file:
        c = int.from_bytes(binary_file.read())
        m_chunks.append(pow(c, d, n))

    with open(r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\decrypted_files\msg.png", "wb") as file:
        for m in m_chunks:
            file.write(m.to_bytes(N, 'big'))
