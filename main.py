from tkinter import *
from matplotlib import pyplot as plt
from liner_congurent_generator import *

import matplotlib
matplotlib.use('TkAgg')

def generate_number():
    global number
    global entry
    number = random(int(entry.get()))
    number_var.set("Random number: " + str(number))


def generate_and_show():
    global entry
    size = 25
    m = pow(2, 32)

    numbers = normalized_lcg(pow(2, 7), pow(2, 8) - 1, m, 69069, 0, int(entry.get()), size)

    plt.hist(numbers, bins=50, range=(pow(2, 7), pow(2, 8)), edgecolor='black', alpha=0.7)
    plt.title("Histogram LCG generiranih števil")
    plt.xlabel("Vrednost")
    plt.ylabel("Frekvenca pojavitve")
    plt.show()


if __name__ == "__main__":
    root = Tk()

    root.title("Praštevila in RSA")
    root.geometry('300x200')

    title = Label(root, text="Generiraj praštevilo")
    title.pack()

    label = Label(root, text="Vnesi seme", font="Courier 12")
    label.pack()

    entry = Entry(root, width=40)
    entry.focus_set()
    entry.pack()

    number_var = StringVar()
    number_var.set("Random number: N/A")

    button = Button(root, text='Generate', width=25, command=generate_number)
    button.pack()

    histogram_button = Button(root, text='Generate numbers on histogram', width=25, command=generate_and_show)
    histogram_button.pack()

    button = Button(root, text='Exit', width=25, command=root.destroy)
    button.pack()

    number_label = Label(root, textvariable=number_var, font="Courier 12")  # Bind to StringVar
    number_label.pack()

    root.mainloop()
