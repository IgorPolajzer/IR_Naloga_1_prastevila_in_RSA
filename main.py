from tkinter import *
from matplotlib import pyplot as plt
from functions import *
import time

import matplotlib

matplotlib.use('TkAgg')


def generate_number():
    global seed, min_val, max_val

    try:
        if int(min_val.get()) < int(max_val.get()):
            numbers = random(int(min_val.get()), int(max_val.get()), int(seed.get()))
            result_var.set("Random number: " + str(numbers[-1]))
    except ValueError:
        result_var.set("Invalid input for 'Seed', 'Min number' or 'Max number'")


def generate_and_show():
    global seed, min_val, max_val

    try:
        if int(min_val.get()) < int(max_val.get()):
            numbers = random(int(min_val.get()), int(max_val.get()), int(seed.get()))

            hist, bins = np.histogram(numbers, bins=int(max_val.get()), range=(int(min_val.get()), int(max_val.get())))
            plt.bar(bins[:-1], hist, width=np.diff(bins), edgecolor='black', alpha=0.7)
            plt.title("Hystogram of LCG generated numbers")
            plt.xlabel("Value")
            plt.ylabel("Frequency")
            plt.show()
    except ValueError:
        result_var.set("Invalid input for 'Seed', 'Min number' or 'Max number'")


def test_number_naive():
    global p_input
    try:
        p = int(p_input.get())
        p, result = naive_test(p)
        result_var.set(f"Naive Test Result: {result}")
    except ValueError:
        result_var.set("Invalid input for 'Number'")


def test_number_miller_rabin():
    global p_input, s_input
    try:
        p = int(p_input.get())
        s = int(s_input.get())
        result = miller_rabin_test(p, s)
        result_var.set(f"Naive Test Result: {result}")
    except ValueError:
        result_var.set("Invalid input for 'Number' or 'Reliability'")


def generate_naive():
    global n_input
    try:
        n = int(n_input.get())
        p = generate_prime_naive(n)
        result_var.set(f"Generated number: {p}")
    except ValueError:
        result_var.set("Invalid input for 'Max number of bits'")

def generate_miller_rabin():
    global n_input, s_input
    try:
        n = int(n_input.get())
        s = int(s_input.get())
        p = generate_prime_miller_rabin(n, s)
        result_var.set(f"Generated number: {p}")
    except ValueError:
        result_var.set("Invalid input for 'Max number of bits' or 'Reliability'")


def measure_time_and_plot():
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
                total_numbers += generate_prime_naive(i)
            elif miller_rabin_var.get():
                total_numbers += generate_prime_miller_rabin(i, 10)

            total_time += (time.time() - start)

        numbers_avg.append(total_numbers / iterations)
        time_avg.append(total_time / iterations)

    plt.plot(numbers_avg, time_avg)
    plt.show()



if __name__ == "__main__":
    root = Tk()

    root.title("Prime number generator")
    root.geometry('600x750')

    # Title.
    title = Label(root, text="Prime number generator", font=("Arial", 14, "bold"))
    title.pack(pady=10)

    # Input Frame.
    input_frame = Frame(root, padx=10, pady=10)
    input_frame.pack(fill=X)

    Label(input_frame, text="Seed: ", font=("Courier", 10)).grid(row=1, column=0, sticky=W, pady=10)
    seed = Entry(input_frame, width=30)
    seed.grid(row=1, column=2, pady=5)

    Label(input_frame, text="Min number: ", font=("Courier", 10)).grid(row=2, column=0, sticky=W, pady=10)
    min_val = Entry(input_frame, width=30)
    min_val.grid(row=2, column=2, pady=5)

    Label(input_frame, text="Max number: ", font=("Courier", 10)).grid(row=3, column=0, sticky=W, pady=10)
    max_val = Entry(input_frame, width=30)
    max_val.grid(row=3, column=2, pady=5)

    Label(input_frame, text="Number: ", font=("Courier", 10)).grid(row=4, column=0, sticky=W, pady=10)
    p_input = Entry(input_frame, width=30)
    p_input.grid(row=4, column=2, pady=5)

    Label(input_frame, text="Reliability: ", font=("Courier", 10)).grid(row=5, column=0, sticky=W, pady=10)
    s_input = Entry(input_frame, width=30)
    s_input.grid(row=5, column=2, pady=5)

    Label(input_frame, text="Max number of bits: ", font=("Courier", 10)).grid(row=6, column=0, sticky=W, pady=10)
    n_input = Entry(input_frame, width=30)
    n_input.grid(row=6, column=2, pady=5)

    # Buttons Frame.
    button_frame = Frame(root, padx=10, pady=10)
    button_frame.pack(fill=X)

    Button(button_frame, text='Generate Random Number', width=25, command=generate_number).pack(pady=5)
    Button(button_frame, text='Generate Histogram', width=25, command=generate_and_show).pack(pady=5)
    Button(button_frame, text='Test Naive', width=25, command=test_number_naive).pack(pady=5)
    Button(button_frame, text='Test Miller-Rabin', width=25, command=test_number_miller_rabin).pack(pady=5)
    Button(button_frame, text='Generate Naive', width=25, command=generate_naive).pack(pady=5)
    Button(button_frame, text='Generate Miller-Rabin', width=25, command=generate_miller_rabin).pack(pady=5)

    # Measure Time and Plot Frame.
    plot_frame = Frame(button_frame, padx=10, pady=10)
    plot_frame.pack(pady=5)

    naive_var = IntVar()
    miller_rabin_var = IntVar()

    Button(plot_frame, text='Measure Time and Plot', width=25, command=measure_time_and_plot).pack(pady=5)
    Checkbutton(plot_frame, text="Naive", variable=naive_var).pack(side=LEFT, padx=5)
    Checkbutton(plot_frame, text="Miller-Rabin", variable=miller_rabin_var).pack(side=LEFT, padx=5)

    Button(button_frame, text='Exit', width=25, command=root.destroy).pack(pady=5)

    # Output Label
    result_var = StringVar()
    result_var.set("Result: N/A")
    result_label = Label(root, textvariable=result_var, font=("Courier", 12))
    result_label.pack(pady=10)

    root.mainloop()
