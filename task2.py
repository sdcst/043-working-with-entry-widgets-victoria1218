#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import math


def run(e):
    data1 = e1.get()
    data2 = e2.get()
    data1 = float(data1)
    data2 = float(data2)
    data = round(math.sqrt((data1**2) + (data2**2)), 2)
    l3.config(text=data)
    e3.delete(0,tk.END)
    e3.insert(0,data)

win = tk.Tk()
l4 = tk.Label(win, text="Please enter two shortsides of a right triangle in order to calculate its hypoteneuse")
l1 = tk.Label(win, text="Short Side 1")
l2 = tk.Label(win, text="Short Side 2")
l3 = tk.Label(win, text="Hypoteneuse:")
e1 = tk.Entry(win,width=15)
b1 = tk.Button(win, text="Calculate")
e2 = tk.Entry(win, width=15)
e3 = tk.Entry(win, width=15)



b1.bind("<Button-1>",run)

l4.grid(row=1, column=1, columnspan=2)
l1.grid(row=2, column=1)
e1.grid(row=3, column=1)
l2.grid(row=2, column=2)
e2.grid(row=3, column=2)
b1.grid(row=4, column=1)
l3.grid(row=4, column=2)
e3.grid(row=5, column=2)

win.mainloop()


