# Import Module
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from liner_congurent_generator import lcg;

def generate_and_shot():
    size = 10000
    plt.hist(lcg(pow(2, 32), 69069, 0, 1, size), bins=50, edgecolor='black', alpha=0.7)
    plt.title("Histogram LCG generiranih števil")
    plt.xlabel("Vrednost")
    plt.ylabel("Freakvenca pojavitve")
    plt.show()

# create root window
root = Tk()

# root window title and dimension
root.title("Praštevila in RSA")
# Set geometry (widthxheight)
root.geometry('350x200')

title = Label(root, text="Generiraj praštevilo")
title.pack()

button = Button(root, text='Generate', width=25, command=generate_and_shot)
button.pack()

button = Button(root, text='Exit', width=25, command=root.destroy)
button.pack()

# all widgets will be here
# Execute Tkinter
root.mainloop()