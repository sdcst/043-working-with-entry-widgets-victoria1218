"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk 

def run(e):
    data1 = e1.get()
    data2 = e2.get()
    data3 = e3.get()
    data = "Name: " + data1 +"\n " + "Student Number: " + data2 + "\n" + "Grade: " + data3
    l4.config(text=data)
    e4.delete(0,tk.END)
    e4.insert(0,data)

win = tk.Tk()
l1 = tk.Label(win, text="Name")
l2 = tk.Label(win, text="Student Number")
l3 = tk.Label(win, text="Grade")
e1 = tk.Entry(win,width=15)
b1 = tk.Button(win, text="Click to save information")
e2 = tk.Entry(win, width=15)
e3 = tk.Entry(win, width=15)
e4 = tk.Entry(win,width=15)
l4 = tk.Label(win,text="New Information")


b1.bind("<Button-1>",run)

l1.grid(row=1, column=1)
e1.grid(row=2, column=1)
l2.grid(row=1, column=2)
e2.grid(row=2, column=2)
l3.grid(row=1, column=3)
e3.grid(row=2, column=3)
b1.grid(row=3, column=2)
l4.grid(row=4, column=1, columnspan=3, rowspan=3)
win.mainloop()