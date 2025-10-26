from math import ceil, log, floor


def modular_exponantion(a, b, n) -> int:
    d = 1
    bodi = int_to_binary_array(b)

    for b in bodi[::-1]:
        d = pow(d, 2) % n

        if b == 1:
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

    # Convert bits to bytes
    N_bytes = ceil(N / 8)

    chunks = read_file_in_binary(file_path, M)

    with open(
            r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\encryptet_files\enc.bin",
            "wb") as binary_file:
        for chunk in chunks:
            c = pow(chunk, e, n)  # modular_exponantion(chunk, e, n)
            binary_file.write(c.to_bytes(N_bytes, 'big'))


def decrypt_and_write_file(file_path: str, s_key):
    d, n = s_key

    M = floor(log(n, 2))
    N = ceil(log(n, 2))

    # Convert bits to bytes
    N_bytes = ceil(N / 8)

    m_chunks = []

    # Decrypt into M-bit chunks
    with open(file_path, "rb") as binary_file:
        while True:
            chunk_bytes = binary_file.read(N_bytes)
            if not chunk_bytes:
                break

            c = int.from_bytes(chunk_bytes, 'big')
            m = pow(c, d, n)
            m_chunks.append(m)

    bit_buffer = 0  # Bits to be written
    bits_in_buffer = 0  # Number of bits in buffer

    with open(
            r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\decrypted_files\msg.png",
            "wb") as file:

        for m in m_chunks:
            bit_buffer = (bit_buffer << M) | m
            bits_in_buffer += M

            # When bits_in_buffer can be written as a byte
            while bits_in_buffer >= 8:
                # Bit shift needed to align the next byte to the right
                shift_amount = bits_in_buffer - 8

                # Extract the highest 8 bits
                byte_to_write = (bit_buffer >> shift_amount) & 0xFF

                # Write the complete byte to the file
                file.write(byte_to_write.to_bytes(1, 'big'))

                # Remove the 8 bits that were just written
                bit_buffer &= (1 << shift_amount) - 1
                bits_in_buffer -= 8

        # Handle the remainder.
        if bits_in_buffer > 0:
            padding_bits = 8 - bits_in_buffer
            final_byte = bit_buffer << padding_bits
            file.write(final_byte.to_bytes(1, 'big'))
