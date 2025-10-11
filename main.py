from tkinter import *
from matplotlib import pyplot as plt
from liner_congurent_generator import *

import matplotlib

matplotlib.use('TkAgg')


def generate_number():
    global seed, min_val, max_val

    try:
        if int(min_val.get()) < int(max_val.get()):
            numbers = random(int(min_val.get()), int(max_val.get()), int(seed.get()))
            number_var.set("Random number: " + str(numbers[-1]))
    except ValueError:
        pass


def generate_and_show():
    global seed, min_val, max_val

    try:
        if int(min_val.get()) < int(max_val.get()):
            numbers = random(int(min_val.get()), int(max_val.get()), int(seed.get()))

            plt.hist(numbers, bins=int(max_val.get()), range=(int(min_val.get()), int(max_val.get())),
                     edgecolor='black', alpha=0.7)
            plt.title("Histogram LCG generiranih števil")
            plt.xlabel("Vrednost")
            plt.ylabel("Frekvenca pojavitve")
            plt.show()
    except ValueError:
        pass


if __name__ == "__main__":
    root = Tk()

    root.title("Praštevila in RSA")
    root.geometry('400x380')

    # Title
    title = Label(root, text="Generiraj praštevilo", font=("Arial", 14, "bold"))
    title.pack(pady=10)

    # Input Frame
    input_frame = Frame(root, padx=10, pady=10)
    input_frame.pack(fill=X)

    Label(input_frame, text="Vnesi seme", font=("Courier", 12)).grid(row=0, column=0, sticky=W, pady=5)
    seed = Entry(input_frame, width=30)
    seed.grid(row=0, column=1, pady=5)

    Label(input_frame, text="Min", font=("Courier", 10)).grid(row=1, column=0, sticky=W, pady=5)
    min_val = Entry(input_frame, width=30)
    min_val.grid(row=1, column=1, pady=5)

    Label(input_frame, text="Max", font=("Courier", 10)).grid(row=2, column=0, sticky=W, pady=5)
    max_val = Entry(input_frame, width=30)
    max_val.grid(row=2, column=1, pady=5)

    # Buttons Frame
    button_frame = Frame(root, padx=10, pady=10)
    button_frame.pack(fill=X)

    Button(button_frame, text='Generate', width=25, command=generate_number).pack(pady=5)
    Button(button_frame, text='Generate numbers on histogram', width=25, command=generate_and_show).pack(pady=5)
    Button(button_frame, text='Exit', width=25, command=root.destroy).pack(pady=5)

    # Output Label
    number_var = StringVar()
    number_var.set("Random number: N/A")
    number_label = Label(root, textvariable=number_var, font=("Courier", 12))
    number_label.pack(pady=10)

    root.mainloop()
