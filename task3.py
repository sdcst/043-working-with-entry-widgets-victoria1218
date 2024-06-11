#!python3

"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""

import tkinter as tk

w = tk.Tk()
w.attributes("-topmost",True)

l = []
l.append( tk.Label(w,text="Number 1"))
l.append( tk.Label(w,text="Number 2"))
l.append( tk.Label(w,text="Number Calculator"))


e = []
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text="answer",state='disabled'))
b=[]
b.append(tk.Button(w,text="x"))
b.append(tk.Button(w,text="+"))
b.append(tk.Button(w,text="-"))
b.append(tk.Button(w,text="÷"))

l[2].grid(row=1,column=1,columnspan=4)
l[0].grid(row=2,column=1,columnspan=2)
l[1].grid(row=2,column=3,columnspan=2)
b[0].grid(row=3,column=1)
b[1].grid(row=3,column=2)
b[2].grid(row=3,column=3)
b[3].grid(row=3,column=4)
e[2].grid(row=4,column=1,columnspan=4)

w.mainloop()

import tkinter as tk

def addition(value=False):
    global e
    try:
        print(value)
        num1 = int(e2.get())
        num2 = int(e3.get())
        e[2].config(text=(num1+num2))
        e[3].delete(0,tk.END)
        e[3].insert(0,(num1+num2))
        
        
        
    except Exception as f:
        print(f)
def sub(value=False):
    global e
    try:
        print(value)
        num1 = int(e2.get())
        num2 = int(e3.get())
        e[2].config(text=(num1-num2))
        e[3].delete(0,tk.END)
        e[3].insert(0,(num1-num2))
        
        
    except Exception as f:
        print(f)
def mult(value=False):
    global e
    try:
        print(value)
        num1 = int(e2.get())
        num2 = int(e3.get())
        e[2].config(text=(num1*num2))
        e[3].delete(0,tk.END)
        e[3].insert(0,(num1*num2))
        
        
    except Exception as f:
        print(f)
def div(value=False):
    global e
    try:
        print(value)
        num1 = int(e2.get())
        num2 = int(e3.get())
        e[2].config(text=(num1/num2))
        e[3].delete(0,tk.END)
        e[3].insert(0,(num1/num2))
        
        
    except Exception as f:
        print(f)



w = tk.Tk()

w.attributes("-topmost",True)

l = []
l.append( tk.Label(w,text="Number 1"))
l.append( tk.Label(w,text="Number 2"))
l.append( tk.Label(w,text="Number Calculator"))


e = []
e.append( tk.Entry(w,text="", width=15))
e.append( tk.Entry(w,text="", width=15))
e.append( tk.Label(w,text=""))
e.append( tk.Entry(w, text="", width=15))

b=[]
b.append(tk.Button(w,text="x",))
b.append(tk.Button(w,text="+"))
b.append(tk.Button(w,text="-"))
b.append(tk.Button(w,text="÷"))
e2 = tk.Entry(w, width=15)
e3 = tk.Entry(w, width=15)

b[0].bind("<Button-1>",mult)
b[1].bind("<Button-1>",addition)
b[2].bind("<Button-1>",sub)
b[3].bind("<Button-1>",div)

l[2].grid(row=1,column=1,columnspan=4)
b[0].grid(row=4,column=1)
b[1].grid(row=4,column=2)
b[2].grid(row=4,column=3)
b[3].grid(row=4,column=4)
e[2].grid(row=5,column=1,columnspan=4)
e[3].grid(row=6,column=1)



