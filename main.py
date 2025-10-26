import os
from tkinter import *
from tkinter import filedialog

from matplotlib import pyplot as plt

from clear import directories, clear_directory
from algorithm import *
import time

import matplotlib

matplotlib.use('TkAgg')


def generate_random_number_gui():
    global seed, min_val, max_val

    try:
        if int(min_val.get()) < int(max_val.get()):
            numbers = random(int(min_val.get()), int(max_val.get()), int(seed.get()))
            result_var.set("Random number: " + str(numbers[-1]))
    except ValueError:
        result_var.set("Invalid input for 'Seed', 'Min number' or 'Max number'")


def generate_histogram_gui():
    global seed, min_val, max_val

    try:
        if int(min_val.get()) < int(max_val.get()):
            numbers = random(int(min_val.get()), int(max_val.get()), int(seed.get()))

            hist, bins = np.histogram(numbers, bins=int(max_val.get()), range=(int(min_val.get()), int(max_val.get())))
            plt.bar(bins[:-1], hist, width=np.diff(bins), edgecolor='black', alpha=0.7)
            plt.title("Histogram of LCG generated numbers")
            plt.xlabel("Value")
            plt.ylabel("Frequency")
            plt.show()
    except ValueError:
        result_var.set("Invalid input for 'Seed', 'Min number' or 'Max number'")


def test_naive_gui():
    global p_input
    try:
        p = int(p_input.get())
        p, result = is_prime_naive(p)
        result_var.set(f"Naive Test Result: {result}")
    except ValueError:
        result_var.set("Invalid input for 'Number'")


def test_miller_rabin_gui():
    global p_input, s_input
    try:
        p = int(p_input.get())
        s = int(s_input.get())
        result = is_prime_miller_rabin(p, s, 1)
        result_var.set(f"Naive Test Result: {result}")
    except ValueError:
        result_var.set("Invalid input for 'Number' or 'Reliability'")


def generate_naive_prime_gui():
    global n_input
    try:
        n = int(n_input.get())
        p = generate_prime_naive_method(n)
        result_var.set(f"Generated number: {p}")
    except ValueError:
        result_var.set("Invalid input for 'Max number of bits'")


def generate_miller_rabin_prime_gui():
    global n_input, s_input
    try:
        n = int(n_input.get())
        s = int(s_input.get())
        p = generate_prime_miller_rabin(n, s)
        result_var.set(f"Generated number: {p}")
    except ValueError:
        result_var.set("Invalid input for 'Max number of bits' or 'Reliability'")


def plot_generation_time_gui():
    global naive_var, miller_rabin_var

    if naive_var.get() and miller_rabin_var.get():
        result_var.set("Only one algortihm at a time can be selected.")
        return

    if not naive_var.get() and not miller_rabin_var.get():
        result_var.set("An algorithm has to be selected.")
        return

    numbers_avg = []
    time_avg = []

    for i in range(4, 33):
        total_time = 0
        total_numbers = 0
        iterations = 3

        for j in range(1, iterations):
            start = time.time()

            if naive_var.get():
                total_numbers += generate_prime_naive_method(i)
            elif miller_rabin_var.get():
                total_numbers += generate_prime_miller_rabin(i, 10)

            total_time += (time.time() - start)

        numbers_avg.append(total_numbers / iterations)
        time_avg.append(total_time / iterations)

    plt.plot(numbers_avg, time_avg)
    plt.show()


def generate_rsa_key_gui():
    global n_input, naive_var, miller_rabin_var

    try:
        # file_path = filedialog.askdirectory()
        file_path = r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\keys"

        n = int(n_input.get())

        if naive_var.get() and miller_rabin_var.get():
            result_var.set("Only one algortihm at a time can be selected.")
            return

        if not naive_var.get() and not miller_rabin_var.get():
            result_var.set("An algorithm has to be selected.")
            return

        if naive_var.get():
            store_rsa_keys(n, file_path, Algorithm.NAIVE)
            result_var.set(f"Keys generated with Naive method stored in folder: {file_path}")

        elif miller_rabin_var.get():
            store_rsa_keys(n, file_path, Algorithm.MILLER_RABIN)
            result_var.set(f"Keys generated with Miller-Rabin method and stored in folder: {file_path}")

    except ValueError:
        result_var.set("Invalid input for 'Max number of bits''")


def plot_key_generation_gui():
    global naive_var, miller_rabin_var

    if naive_var.get() and miller_rabin_var.get():
        result_var.set("Only one algortihm at a time can be selected.")
        return

    if not naive_var.get() and not miller_rabin_var.get():
        result_var.set("An algorithm has to be selected.")
        return

    execution_times = []
    bit_size = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    for i in bit_size:
        start_time = time.time()
        if naive_var.get():
            generate_rsa_key_pair(i, Algorithm.NAIVE)

        elif miller_rabin_var.get():
            generate_rsa_key_pair(i, Algorithm.MILLER_RABIN)
        execution_times.append(time.time() - start_time)

    plt.plot(bit_size, execution_times)
    plt.xlabel('Histogram of RSA Key generation')
    plt.ylabel('Time (seconds)')
    plt.title('Bit size of RSA key')
    plt.show()


def plot_encryption_gui():

    avg_enc_execution_times = []
    avg_dec_execution_times = []
    key_folder_path = r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\keys"
    file_path = r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\test_files\number.txt"

    bit_sizes = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    ro = 1

    for n in bit_sizes:
        store_rsa_keys(n, key_folder_path, Algorithm.NAIVE)

        iterations = 10
        enc_execution_times = []
        dec_execution_times = []

        for _ in range(iterations):
            # Generate a random number within the range for the current bit size
            max_range = pow(2, n) - 1
            number = random(0, max_range, ro, NUMBERS_COUNT)[-1]
            ro += 1

            # Write the random number to a file in binary format
            with open(file_path, 'wb') as fp:
                fp.write(number)

            # Measure encryption time
            start_encrypt_time = time.time()
            rsa_encrypt_file(file_path, key_folder_path)
            enc_execution_times.append(time.time() - start_encrypt_time)

            # Measure decryption time
            start_decrypt_time = time.time()
            rsa_decrypt_file(file_path, key_folder_path)
            dec_execution_times.append(time.time() - start_decrypt_time)

        # Calculate average times for the current bit size
        avg_enc_execution_times.append(sum(enc_execution_times) / len(enc_execution_times))
        avg_dec_execution_times.append(sum(dec_execution_times) / len(dec_execution_times))

    # Plot encryption/decryption times
    plt.figure(figsize=(10, 6))  # Opcijsko: večja slika
    plt.plot(bit_sizes, avg_enc_execution_times, label="Encryption Time", marker='o', color='blue')
    plt.plot(bit_sizes, avg_dec_execution_times, label="Decryption Time", marker='s', color='orange')

    plt.xlabel('Bit Size of RSA Key and encrypted number')
    plt.ylabel('Time (seconds)')
    plt.title('RSA Encryption & Decryption Time vs Bit Size')
    plt.grid(True)
    plt.legend()
    plt.show()

def encrypt_file_gui():
    file_path = filedialog.askopenfilename()

    # key_folder_path = filedialog.askdirectory()
    key_folder_path = r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\keys"

    if not os.path.exists(key_folder_path + PUBLIC_KEY_FILE_NAME) or not os.path.exists(
            key_folder_path + PRIVATE_KEY_FILE_NAME):
        result_var.set(f"Private or public key not present in ${key_folder_path}")
        return

    rsa_encrypt_file(file_path, key_folder_path)
    result_var.set(f"File: '{file_path}' was encrypted.")


def decrypt_file_gui():
    # file_path = filedialog.askopenfilename()
    file_path = r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\encryptet_files\enc.bin"

    # key_folder_path = filedialog.askdirectory()
    key_folder_path = r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\keys"

    if not os.path.exists(key_folder_path + PUBLIC_KEY_FILE_NAME) or not os.path.exists(
            key_folder_path + PRIVATE_KEY_FILE_NAME):
        result_var.set(f"Private or public key not present in ${key_folder_path}")
        return

    if not os.path.exists(file_path):
        result_var.set(f"The file you are trying to decode doesnt exist")
        return

    rsa_decrypt_file(file_path, key_folder_path)
    result_var.set(f"File: '{file_path}' was decrypted.")


def clear_directories_gui():
    for dir_path in directories:
        clear_directory(dir_path)

    result_var.set("Directories cleared successfully.")


if __name__ == "__main__":
    root = Tk()

    root.title("Prime number generator")
    root.geometry('700x1000')

    # Title.
    title = Label(root, text="Prime number generator", font=("Arial", 14, "bold"))
    title.pack(pady=10, anchor="center")

    # Input Frame.
    input_frame = Frame(root, padx=10, pady=10)
    input_frame.pack(anchor="center")

    # Configure grid columns to center content
    input_frame.grid_columnconfigure(0, weight=0)
    input_frame.grid_columnconfigure(1, weight=0, minsize=20)
    input_frame.grid_columnconfigure(2, weight=0)

    Label(input_frame, text="Seed: ", font=("Courier", 10)).grid(row=1, column=0, sticky=E, pady=10, padx=(0, 5))
    seed = Entry(input_frame, width=30)
    seed.grid(row=1, column=2, pady=5, sticky=W)

    Label(input_frame, text="Min number: ", font=("Courier", 10)).grid(row=2, column=0, sticky=E, pady=10, padx=(0, 5))
    min_val = Entry(input_frame, width=30)
    min_val.grid(row=2, column=2, pady=5, sticky=W)

    Label(input_frame, text="Max number: ", font=("Courier", 10)).grid(row=3, column=0, sticky=E, pady=10, padx=(0, 5))
    max_val = Entry(input_frame, width=30)
    max_val.grid(row=3, column=2, pady=5, sticky=W)

    Label(input_frame, text="Number: ", font=("Courier", 10)).grid(row=4, column=0, sticky=E, pady=10, padx=(0, 5))
    p_input = Entry(input_frame, width=30)
    p_input.grid(row=4, column=2, pady=5, sticky=W)

    Label(input_frame, text="Reliability: ", font=("Courier", 10)).grid(row=5, column=0, sticky=E, pady=10, padx=(0, 5))
    s_input = Entry(input_frame, width=30)
    s_input.grid(row=5, column=2, pady=5, sticky=W)

    Label(input_frame, text="Max number of bits: ", font=("Courier", 10)).grid(row=6, column=0, sticky=E, pady=10,
                                                                               padx=(0, 5))
    n_input = Entry(input_frame, width=30)
    n_input.grid(row=6, column=2, pady=5, sticky=W)

    # Buttons Frame.
    button_frame = Frame(root, padx=10, pady=10)
    button_frame.pack(anchor="center")

    Button(button_frame, text='Generate Random Number', width=25, command=generate_random_number_gui).pack(pady=5)
    Button(button_frame, text='Generate Histogram', width=25, command=generate_histogram_gui).pack(pady=5)
    Button(button_frame, text='Test Naive', width=25, command=test_naive_gui).pack(pady=5)
    Button(button_frame, text='Test Miller-Rabin', width=25, command=test_miller_rabin_gui).pack(pady=5)
    Button(button_frame, text='Generate Naive', width=25, command=generate_naive_prime_gui).pack(pady=5)
    Button(button_frame, text='Generate Miller-Rabin', width=25, command=generate_miller_rabin_prime_gui).pack(pady=5)
    Button(button_frame, text='Generate Keys', width=25, command=generate_rsa_key_gui).pack(pady=5)
    Button(button_frame, text='Encrypt file', width=25, command=encrypt_file_gui).pack(pady=5)
    Button(button_frame, text='Decrypt file', width=25, command=decrypt_file_gui).pack(pady=5)

    # Measure Time and Plot Frame.
    plot_frame = Frame(button_frame, padx=10, pady=10)
    plot_frame.pack(pady=5, anchor="center")

    naive_var = IntVar()
    miller_rabin_var = IntVar()

    Button(plot_frame, text='Prime Generation Histogram', width=25, command=plot_generation_time_gui).pack(pady=5)
    Button(plot_frame, text='Key Generation Histogram', width=25, command=plot_key_generation_gui).pack(pady=5)
    Button(plot_frame, text='Encryption/Decryption Histogram', width=25, command=plot_encryption_gui).pack(pady=5)

    # Checkbox frame to center checkboxes
    checkbox_frame = Frame(plot_frame)
    checkbox_frame.pack()
    Checkbutton(checkbox_frame, text="Naive", variable=naive_var).pack(side=LEFT, padx=5)
    Checkbutton(checkbox_frame, text="Miller-Rabin", variable=miller_rabin_var).pack(side=LEFT, padx=5)

    Button(button_frame, text='Clear folders', width=25, command=clear_directories_gui).pack(pady=5)
    Button(button_frame, text='Exit', width=25, command=root.destroy).pack(pady=5)

    # Output Label
    result_var = StringVar()
    result_var.set("Result: N/A")
    result_label = Label(root, textvariable=result_var, font=("Courier", 12), wraplength=500, justify="center")
    result_label.pack(padx=10, pady=10, anchor="center")

    root.mainloop()
